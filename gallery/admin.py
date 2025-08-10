from django.contrib import admin
from .models import Gallery, Photo

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'sport', 'event_date', 'created_at')
    search_fields = ('title', 'sport')
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'gallery', 'uploaded_at', 'is_featured')
    list_filter = ('is_featured', 'gallery')
    search_fields = ('title', 'caption')