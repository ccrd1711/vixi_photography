from dataclasses import dataclass

CART_KEY = 'cart'


class CartItem:
    photo: object
    qty: int
    line_total_pence: int


def _get_cart(session):
    return session.get(CART_KEY, {})


def add(session, photo_id, qty=1):
    cart = _get_cart(session)
    cart[str(photo_id)] = cart.get(str(photo_id), 0) + qty
    session[CART_KEY] = cart
    session.modified = True


def remove(session, photo_id):
    cart = _get_cart(session)
    cart.pop(str(photo_id), None)
    session[CART_KEY] = cart
    session.modified = True


def clear(session):
    session.pop(CART_KEY, None)
    session.modified = True
