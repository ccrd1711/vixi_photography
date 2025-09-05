def cart_count(request):
    cart = request.session.get("cart", {})
    total = 0
    for v in cart.values():
        total += int(v.get("qty", 0)) if isinstance(v, dict) else int(v)
    return {"cart_count": total}
