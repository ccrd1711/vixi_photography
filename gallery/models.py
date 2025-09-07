from django.db import models
from django.templatetags.static import static

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    sport = models.CharField(max_length=60, blank=True)
    event_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-event_date', '-created_at']

    def __str__(self):
        return self.title
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    price_pence = models.PositiveIntegerField(default=0)

    image_url = models.CharField(max_length=255, blank=True)        # "photos/photo1.jpg" or "http://example.com/photo1.jpg"    
    download_path = models.CharField(max_length=255, blank=True)        # "downloads/photo1_colour.jpg"
    download_path_bw = models.CharField(max_length=255, blank=True)     # "downloads/photo1_bw.jpg"

    def __str__(self):
        return self.title

    @property
    def download_url(self):
        return self._resolve_static(self.download_path)

    def download_url_for(self, variant: str):
        if variant == "bw" and self.download_path_bw:
            return self._resolve_static(self.download_path_bw)
        return self._resolve_static(self.download_path or "")

    @staticmethod
    def _resolve_static(path: str) -> str:
        if not path:
            return ""
        if path.startswith(("http://", "https://", "/")):
            return path
        return static(path)