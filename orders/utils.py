# orders/utils.py
from gallery.models import Photo
from .models import Order, OrderItem

def create_order_from_session(user, session):
    cart = session.get('cart', {})
    if not cart:
        return None

    order = Order.objects.create(
        user=user if getattr(user, "is_authenticated", False) else None,
        email=(getattr(user, "email", "") or ""),
        status="submitted",   # ✅ make sure new orders start as submitted
    )

    for key, qty in cart.items():
        # qty might be an int or a dict like {"qty": 2}
        if isinstance(qty, dict):
            try:
                qty_val = int(qty.get("qty", 1))
            except (TypeError, ValueError):
                qty_val = 1
        else:
            try:
                qty_val = int(qty)
            except (TypeError, ValueError):
                qty_val = 1

        # key can be "photo_id" or "photo_id:variant"
        variant = "colour"
        pid_str = str(key)
        if isinstance(key, str) and ":" in key:
            pid_str, variant = key.split(":", 1)

        try:
            pid = int(pid_str)
        except ValueError:
            # skip bad cart key
            continue

        photo = Photo.objects.get(pk=pid)

        OrderItem.objects.create(
            order=order,
            photo=photo,
            qty=max(1, qty_val),
            price_each_pence=photo.price_pence,
            variant=variant,
        )

    order.recalc()
    return order
