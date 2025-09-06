from django.contrib import admin
from .models import Gallery, Photo

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "sport", "event_date", "created_at")
    search_fields = ("title", "sport")

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price_pence", "download_path", "download_path_bw")
    search_fields = ("title",)
    fields = ("title", "price_pence", "download_path", "download_path_bw")
