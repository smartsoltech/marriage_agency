# payments/views.py

from django.shortcuts import render, redirect
from .models import TariffPlan, UserSubscription, AdditionalService, UserAdditionalService
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
import stripe
from django.contrib import messages
from datetime import timedelta
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def tariff_plans(request):
    plans = TariffPlan.objects.all()
    return render(request, 'payments/tariff_plans.html', {'plans': plans})

@login_required
def purchase_plan(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        plan = TariffPlan.objects.get(id=plan_id)
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',  # Можно сделать динамическим
                    'product_data': {
                        'name': plan.name,
                    },
                    'unit_amount': int(plan.price * 100),  # Цена в центах
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/'),
            cancel_url=request.build_absolute_uri('/payments/cancel/'),
        )
        return redirect(session.url, code=303)
    else:
        return redirect('tariff_plans')

@login_required
def payments_success(request):
    # Обработка успешной оплаты, например, обновление подписки
    # Для примера просто отправим сообщение
    messages.success(request, _('Payment was successful!'))
    return redirect('tariff_plans')

@login_required
def payments_cancel(request):
    messages.error(request, _('Payment was cancelled.'))
    return redirect('tariff_plans')

@login_required
def additional_services(request):
    services = AdditionalService.objects.all()
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        quantity = int(request.POST.get('quantity', 1))
        service = AdditionalService.objects.get(id=service_id)
        UserAdditionalService.objects.create(user=request.user, service=service, quantity=quantity)
        messages.success(request, _('Additional service purchased successfully!'))
        return redirect('additional_services')
    return render(request, 'payments/additional_services.html', {'services': services})

@login_required
def payment_view(request):
    if request.method == 'POST':
        amount = 5000  # 50.00 USD, пример
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description="Test Charge",
                source=request.POST['stripeToken']
            )
            Payment.objects.create(user=request.user, stripe_charge_id=charge.id, amount=amount / 100)
            return redirect('payment_success')
        except stripe.error.StripeError:
            return redirect('payment_failure')
    return render(request, 'payments/payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_failure(request):
    return render(request, 'payments/failure.html')