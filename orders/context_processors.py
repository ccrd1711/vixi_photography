def cart_count(request):
    cart = request.session.get('cart', {})
    return {"cart_count": sum(cart.values())} # ADD TO CART PAGE WHEN FULLY IMPLEMENTED 
