from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:photo_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:photo_id>/", views.remove_from_cart,
         name="remove_from_cart"),
    path("cart/remove-one/<int:photo_id>/", views.remove_one,
         name="remove_one"),
    path("checkout/", views.checkout, name="checkout"),
    path("success/", views.checkout_success, name="checkout_success"),
    path("cancel/", views.checkout_cancel, name="checkout_cancel"),
    path("orders/", views.my_orders, name="my_orders"),
    path("download/<int:item_id>/", views.download_item, name="download_item"),
    path("book/", views.book_request, name="book_request"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/edit/", views.edit_booking, name="edit_booking"),
    path("bookings/<int:pk>/cancel/", views.delete_booking,
         name="delete_booking"),
    path("bookings/<int:pk>/deposit/", views.booking_deposit_checkout,
         name="booking_deposit_checkout"),
    path("bookings/<int:pk>/deposit/success/", views.booking_deposit_success,
         name="booking_deposit_success"),
    path("bookings/<int:pk>/deposit/cancel/", views.booking_deposit_cancel,
         name="booking_deposit_cancel"),
]
