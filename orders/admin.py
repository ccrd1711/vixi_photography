from django.contrib import admin
from .models import Order, OrderItem, BookingRequest


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ("photo", "qty", "price_each_pence")
    readonly_fields = ()
    show_change_link = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_pence", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("id", "user__username", "user__email")
    date_hierarchy = "created_at"
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "photo", "variant",
                    "qty", "price_each_pence")
    list_filter = ("variant", "order__status",)
    search_fields = ("order__id", "photo__title", "order__user__username")


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event_date", "location",
                    "status", "created_at")
    list_filter = ("status", "event_date", "created_at")
    search_fields = ("user__username", "location")
    date_hierarchy = "created_at"
