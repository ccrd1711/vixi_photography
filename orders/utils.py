from .models import Order, OrderItem
from gallery.models import Photo

def create_order_from_session(user, session):
    cart = session.get("cart", {})
    if not cart:
        return None

    order = Order.objects.create(user=user, status="submitted", email=(user.email if user and user.is_authenticated else ""))

    total = 0
    for key, val in cart.items():
        # support both old format (int qty) and new (dict with variant)
        if isinstance(val, dict):
            qty = int(val.get("qty", 0))
            variant = val.get("variant", "colour")
            photo_id = key.split(":", 1)[0]
        else:
            qty = int(val)
            variant = "colour"
            photo_id = key

        if qty <= 0:
            continue

        photo = Photo.objects.get(pk=int(photo_id))
        price = photo.price_pence

        OrderItem.objects.create(
            order=order,
            photo=photo,
            qty=qty,
            price_each_pence=price,
            variant=variant,
        )
        total += qty * price

    order.total_pence = total
    order.save(update_fields=["total_pence"])
    return order