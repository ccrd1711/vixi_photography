from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("success/", views.checkout_success, name="checkout_success"),
    path("cancel/", views.checkout_cancel, name="checkout_cancel"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:photo_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:photo_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("book/", views.book_request, name="book_request"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/edit/", views.edit_booking, name="edit_booking"),
    path("bookings/<int:pk>/delete/", views.delete_booking, name="delete_booking"),
    path("orders/", views.my_orders, name="my_orders"),
    path("download/<int:item_id>/", views.download_item, name="orderitem_download"),
]