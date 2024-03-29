from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from . import forms
from . import models
from app_users.models import Profile


@login_required(login_url='login')
def pre_pay(request, pk):
    invoice_owner = request.user.profile
    invoice = invoice_owner.owner_invoices.get(id=pk)

    if request.method == 'POST':
        amount = int(request.POST.get('pre_pay_amount'))
        invoice.amount = invoice.amount - amount
        invoice.save()
        messages.success(request, f'{amount} miqdordagi summa asosiy qarzdan ayrildi')
        return redirect('invoices')

    context = {
        'invoice': invoice,
    }
    return render(request, 'app_main/pre_pay.html', context)


@login_required(login_url='signin')
def index_view(request):
    context = {
        'page': 'Admin panel',
        'form_name': 'profile',
        'form_value': '',
        'form_placeholder': 'Username, Ism, Familiya yoki tel. raqam',
        'ads': models.News.objects.all(),
        'total_users_count': User.objects.all().count(),
        'total_invoices': models.Invoice.objects.aggregate(total=Sum('amount')),
    }
    return render(request, 'app_main/index.html', context)


@login_required(login_url='signin')
def confirm_invoice(request, pk):
    profile = request.user.profile
    invoice = profile.sender_invoices.get(id=pk)
    invoice.is_confirmed = True
    invoice.save()
    return redirect('home')


@login_required(login_url='signin')
def invoice_view(request):
    context = {
        'profile': request.user.profile,
        'page': 'Qarzlar',
        'form_name': 'invoice',
        'form_value': '',
        'form_placeholder': 'Username, Ism, Familiya yoki tel. raqam',
    }
    return render(request, 'app_main/tables.html', context)


@login_required(login_url='signin')
def add_invoice(request):
    profile_query = ''
    user_profiles = []
    invoice_requests = request.user.profile.sender_invoices.all()
    if request.GET.get('profile'):
        profile_query = request.GET.get('profile')
        user_profiles = Profile.objects.filter(
            Q(fullname__icontains=profile_query) |
            Q(user__username__icontains=profile_query) |
            Q(inn_number__icontains=profile_query) |
            Q(tel_number__icontains=profile_query) |
            Q(passport_number__icontains=profile_query)
        ).exclude(user=request.user).distinct()

    context = {
        'is_invoice_requests': True if len(invoice_requests) > 0 else False,
        'invoice_requests': invoice_requests,
        'profiles': user_profiles,
        'form_name': 'profile',
        'form_value': profile_query,
        'form_placeholder': 'Username, Ism, Familiya yoki tel. raqam',
        'page': 'Qarz olish/Qarz berish',
    }
    return render(request, 'app_main/add_invoice.html', context)


@login_required(login_url='signin')
def create_invoice(request, pk):
    profile_query = ''
    user_profiles = []
    if request.GET.get('profile'):
        profile_query = request.GET.get('profile')
        user_profiles = Profile.objects.filter(
            Q(fullname__icontains=profile_query) |
            Q(user__username__icontains=profile_query) |
            Q(inn_number__icontains=profile_query) |
            Q(tel_number__icontains=profile_query) |
            Q(passport_number__icontains=profile_query)
        ).exclude(user=request.user).distinct()
    invoice_sender = Profile.objects.get(id=pk)

    if request.method == 'POST':
        form = forms.InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.owner = request.user.profile
            invoice.sender = invoice_sender
            invoice.save()
            messages.success(request,
                             f'{invoice_sender.fullname} ga {form.cleaned_data["amount"]} miqdordagi qarz so`rovi yuborildi')
            return redirect('invoices')
        else:
            messages.error(request, 'Forma noto`g`ri to`ldirildi')
            return redirect('create_invoice')

    form = forms.InvoiceForm()
    context = {
        'invoice_sender': invoice_sender,
        'form': form,
        'page': 'Qarz olish/Qarz berish',
        'profiles': user_profiles,
        'form_name': 'profile',
        'form_value': profile_query,
        'form_placeholder': 'Username, Ism, Familiya yoki tel. raqam',
    }
    return render(request, 'app_main/invoice_form.html', context)


@login_required(login_url='signin')
def invoice_request_approve(request, pk):
    profile = request.user.profile
    invoice = profile.owner_invoices.get(id=pk)
    invoice.is_confirmed = True
    invoice.save()
    messages.success(request, 'Qarz berildi')
    return redirect('add_invoices')
