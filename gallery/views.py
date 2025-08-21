from django.shortcuts import render
from .models import Photo

def index(request):
    photos = Photo.objects.order_by('-uploaded_at')
    return render(request, "gallery/index.html", {"photos": photos})
