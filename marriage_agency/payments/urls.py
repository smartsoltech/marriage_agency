# payments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.tariff_plans, name='tariff_plans'),
    path('purchase/', views.purchase_plan, name='purchase_plan'),
    path('additional_services/', views.additional_services, name='additional_services'),
    path('checkout/', views.payment_view, name='payment'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),
]
