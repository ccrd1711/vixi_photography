from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .utils import create_order_from_session
from gallery.models import Photo
from . import cart as sc
from .forms import BookingRequestForm
from .models import BookingRequest
from .models import Order, OrderItem
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

PRODUCT_NAME = "Mini-shoot booking"
UNIT_AMOUNT = 5000  # £50.00

# CART
def cart_view(request):
    items = []
    total = 0
    for photo_id, qty in request.session.get('cart', {}).items():
        photo = get_object_or_404(Photo, pk=int(photo_id))
        line_total = int(qty) * photo.price_pence
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
    if request.method != "POST":
        return redirect("gallery_index")

    cart = request.session.get("cart", {})
    key = str(photo_id)
    cart[key] = int(cart.get(key, 0)) + 1

    request.session["cart"] = cart
    request.session.modified = True

    photo = get_object_or_404(Photo, pk=photo_id)
    messages.success(request, f"Added {photo.title or 'photo'} to basket.")
    return redirect(request.POST.get("next") or "cart")

def remove_from_cart(request, photo_id):
    cart = request.session.get("cart", {})
    key = str(photo_id)
    if key in cart:
        if int(cart[key]) > 1:
            cart[key] = int(cart[key]) - 1
        else:
            del cart[key]
        request.session["cart"] = cart
        request.session.modified = True
        messages.info(request, "Removed from basket.")
    return redirect("cart")

# STRIPE
def checkout(request):
    # Order from cart
    order = create_order_from_session(request.user, request.session)
    if not order:
        messages.error(request, "Your basket is empty.")
        return redirect("cart")

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
    if request.user.is_authenticated:
        latest = Order.objects.filter(user=request.user, status='submitted').order_by('-created_at').first()
        if latest:
            latest.status = 'paid'
            latest.save(update_fields=['status'])
    sc.clear(request.session)
    messages.success(request, "Payment successful! Thank you for your order.")
    return render(request, "orders/success.html")

def checkout_cancel(request):
    messages.info(request, "Payment cancelled. You can try again from your basket.")
    return render(request, "orders/cancel.html")

# BOOKING PLACEHOLDER
@login_required(login_url='/accounts/login/')
def book_request(request):
    if request.method == "POST":
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            br = form.save(commit=False)
            br.user = request.user
            br.save()
            messages.success(request, "Booking request submitted.")
            return redirect("my_bookings")
    else:
        form = BookingRequestForm()
    return render(request, "orders/booking_form.html", {"form": form, "mode": "create"}) 

@login_required
def my_bookings(request):
    bookings = BookingRequest.objects.filter(user=request.user)
    return render(request, "orders/my_bookings.html", {"bookings": bookings})

@login_required
def edit_booking(request, pk):
    br = get_object_or_404(
        BookingRequest, 
        pk=pk, 
        user=request.user, 
        status__in=["new", "review"]
    )
    if request.method == "POST":
        form = BookingRequestForm(request.POST, instance=br)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking request updated.")
            return redirect("my_bookings")
    else:
        form = BookingRequestForm(instance=br)
    
    return render(request, "orders/booking_form.html", {"form": form, "mode": "edit"})
    
@login_required
def delete_booking(request, pk):
    br = get_object_or_404(BookingRequest, pk=pk, user=request.user, status__in=["new", "review"])
    if request.method == "POST":
        br.status = "cancelled"
        br.save(update_fields=["status"])
        messages.info(request, "Booking request cancelled.")
        return redirect("my_bookings")
    return render(request, "orders/booking_confirm_delete.html", {"booking": br})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at').prefetch_related("items", "items__photo")
    return render(request, "orders/my_orders.html", {"orders": orders})

@login_required
def download_item(request, item_id: int):
    item = get_object_or_404(
        OrderItem.objects.select_related("order", "photo"),
        pk=item_id,
        order__user=request.user,
        order__status="paid",
    )
    url = item.photo.download_url
    if not url:
        messages.error(request, "Download unavailable for this item.")
        return redirect("my_orders")
    return redirect(url)
