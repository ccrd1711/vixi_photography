from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("success/", views.checkout_success, name="checkout_success"),
    path("cancel/", views.checkout_cancel, name="checkout_cancel"),
    path("cart/", views.cart_view, name="cart"),
    path("add/<int:photo_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:photo_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("book/", views.book_request, name="book_request"),
]