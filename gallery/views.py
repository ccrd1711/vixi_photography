from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery, Photo 

# Create your views here.
def my_gallery(request):
    galleries = Gallery.objects.all().order_by("-id")
    return render(request, "gallery/index.html", {"galleries": galleries})