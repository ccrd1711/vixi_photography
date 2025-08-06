from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_gallery(request):
    return HttpResponse("Welcome to My Gallery")