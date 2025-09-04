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
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True)
    capton = models.TextField(blank=True)
    image_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    price_pence = models.PositiveIntegerField(default=9000)
    download_path = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def price_display(self):
        return f"£{self.price_pence / 100:.2f}"

    def __str__(self):
        return self.title or f'Photo #{self.pk}'
    
    @property
    def download_url(self):
        return static(self.download_path) if self.download_path else ""