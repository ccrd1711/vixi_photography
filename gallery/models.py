from django.db import models

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

    class Meta:
        ordering = ['-uploaded_at']

    def price_display(self):
        return f"£{self.price_pence / 100:.2f}"

    def __str__(self):
        return self.title or f'Photo #{self.pk}'
    
