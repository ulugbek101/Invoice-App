from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('invoices/', views.invoice_view, name='invoices'),
    path('invoices/add/', views.add_invoice, name='add_invoices'),
    path('invoices/create/<str:pk>/', views.create_invoice, name='create_invoice'),
    path('invoice-approve/<str:pk>/', views.invoice_request_approve, name='invoice_request_approve'),
]
