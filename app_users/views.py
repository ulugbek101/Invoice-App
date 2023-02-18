from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app_main.models import Invoice
from . import forms


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, f'Welcome, {user.username}!')
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('signin')

    context = {}
    return render(request, 'app_users/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been successfully created')
            return redirect('signin')
        else:
            messages.error(request, 'Form filled incorrectly')
            return redirect('signup')

    form = forms.UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'app_users/signup.html', context)


def user_logout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def profile(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
            return redirect('profile')
        else:
            messages.error(request, 'Form filled incorrectly')
            return redirect('profile')
    context = {
        'form': forms.ProfileForm(instance=user_profile),
        'profile': user_profile,
    }
    return render(request, 'app_users/profile.html', context)
