from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_gallery(request):
    data = [
        {
            "title": g.title,
            "sport": g.sport,
            "event_date": g.event_date.isoformat() if g.event_date else None,
            "photos": [p.image_url for p in g.photos.all()],
        }
        for g in Gallery.objects.prefetch_related('photos')[:10]
    ]
    return JsonResponse({"galleries": data})