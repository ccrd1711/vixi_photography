from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator
                    (r'^\+?[0-9\s\-]+$', 'Enter a valid phone number.')]
    )

    def __str__(self):
        return self.display_name or self.user.get_username()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
