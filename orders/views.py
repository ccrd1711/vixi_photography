from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

PRODUCT_NAME = "Mini-shoot booking" #change change?????
UNIT_AMOUNT = 5000  # Amount in pence (GBP). £50.00

def checkout(request):
    session = stripe.checkout.Session.create(
        mode='payment',
        payment_method_types=['card'],
        line_items=[{
            "price_data": {
                "currency": "gbp",
                "product_data": {"name": PRODUCT_NAME},
                "unit_amount": UNIT_AMOUNT,
            },
            "quantity": 1,
        }],
        success_url=request.build_absolute_uri(reverse('checkout_success')),
        cancel_url=request.build_absolute_uri(reverse('checkout_cancel')),
    )
    return redirect(session.url, code=303)

def checkout_success(request):
    return render(request, "orders/success.html")

def checkout_cancel(request):
    return render(request, "orders/cancel.html")
