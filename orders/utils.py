from .models import Order, OrderItem
from gallery.models import Photo

def create_order_from_session(user, session):
    cart = session.get('cart', {})
    if not cart:
        return None
    order = Order.objects.create(user=user, email=getattr(user, "email", "") or "")
    total = 0
    for photo_id, qty in cart.items():
        photo = Photo.objects.get(pk=int(photo_id))
        item = OrderItem.objects.create(
            order=order,
            photo=photo,
            qty=qty,
            price_each_pence=photo.price_pence
        )
        total += item.qty * item.price_each_pence
    order.total_pence = total
    order.status = 'submitted'
    order.save(update_fields=['total_pence', 'status'])
    return order