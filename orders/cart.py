def _cart(session):
    return session.setdefault("cart", {})

def _save(session):
    session.modified = True

def _key(photo_id, variant):

    return f"{int(photo_id)}:{variant or 'colour'}"

def add(session, photo_id, qty=1, variant="colour"):
   
    cart = _cart(session)
    key = _key(photo_id, variant)
    cart[key] = int(cart.get(key, 0)) + int(qty)
    _save(session)

def remove_one(session, photo_id, variant=None):
    
    cart = _cart(session)
    if variant:
        key = _key(photo_id, variant)
        if key in cart:
            cart[key] = int(cart[key]) - 1
            if cart[key] <= 0:
                del cart[key]
            _save(session)
            return
    else:
        
        prefix = f"{int(photo_id)}:"
        for k in list(cart.keys()):
            if k.startswith(prefix):
                cart[k] = int(cart[k]) - 1
                if cart[k] <= 0:
                    del cart[k]
                _save(session)
                return

def remove(session, photo_id, variant=None):

    cart = _cart(session)
    if variant:
        key = _key(photo_id, variant)
        cart.pop(key, None)
    else:
        prefix = f"{int(photo_id)}:"
        for k in [k for k in cart.keys() if k.startswith(prefix)]:
            del cart[k]
    _save(session)

def clear(session):
    session["cart"] = {}
    _save(session)
