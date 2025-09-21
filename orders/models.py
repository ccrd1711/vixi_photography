from django.db import models
from django.conf import settings
from gallery.models import Photo
from django.db.models import Q


class Order(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=12,
                              choices=STATUS_CHOICES, default='draft')
    total_pence = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def recalc(self):
        self.total_pence = sum(i.subtotal_pence for i in self.items.all())
        self.save(update_fields=['total_pence'])

    def total_display(self):
        return f"£{self.total_pence/100:.2f}"

    @property
    def total_pounds(self):
        return self.total_pence / 100


class OrderItem(models.Model):
    VARIANTS = (("colour", "Colour"), ("bw", "Black & White"))

    order = models.ForeignKey("Order",
                              related_name="items", on_delete=models.CASCADE)
    photo = models.ForeignKey("gallery.Photo", on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    price_each_pence = models.PositiveIntegerField()
    variant = models.CharField(max_length=10,
                               choices=VARIANTS, default="colour")

    @property
    def subtotal_pence(self):
        return self.qty * self.price_each_pence

    @property
    def subtotal_display(self):
        return f"£{self.subtotal_pence/100:.2f}"

    def __str__(self):
        return f"{self.photo} x {self.qty} ({self.get_variant_display()})"


class BookingRequest(models.Model):
    STATUS = [
        ("new", "New"),
        ("review", "In Review"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='booking_requests')
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    deposit_pence = models.PositiveIntegerField(default=5000)
    deposit_paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def deposit_display(self):
        return f"£{self.deposit_pence/100:.2f}"

    def __str__(self):
        return f"{self.user} - {self.event_date} - {self.location}"
