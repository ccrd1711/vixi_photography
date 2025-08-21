from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
import stripe

from gallery.models import Photo
from . import cart as sc

stripe.api_key = settings.STRIPE_SECRET_KEY

PRODUCT_NAME = "Mini-shoot booking"
UNIT_AMOUNT = 5000  # £50.00

# ---- CART ----
def cart_view(request):
    items = []
    total = 0
    for photo_id, qty in request.session.get('cart', {}).items():
        photo = get_object_or_404(Photo, pk=int(photo_id))
        line_total = qty * photo.price_pence
        total += line_total
        items.append({
            "photo": photo,
            "qty": qty,
            "line_total_pence": line_total,
            "line_total_display": f"£{line_total/100:.2f}",
        })
    ctx = {
        "items": items,
        "total_pence": total,
        "total_display": f"£{total/100:.2f}",
    }
    return render(request, "orders/cart.html", ctx)

def add_to_cart(request, photo_id):
    sc.add(request.session, photo_id, qty=1)
    messages.success(request, "Added to basket.")
    return redirect(request.POST.get("next") or "cart")

def remove_from_cart(request, photo_id):
    sc.remove(request.session, photo_id)
    messages.info(request, "Removed from basket.")
    return redirect("cart")

# ---- STRIPE (kept from your version) ----
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

# ---- BOOKING PLACEHOLDER ----
def book_request(request):
    return render(request, "orders/book_request.html")