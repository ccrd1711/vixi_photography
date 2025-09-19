from django import forms
from django.core.exceptions import ValidationError
from .models import BookingRequest

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ["event_date", "location", "details"]

    def clean_event_date(self):
        date = self.cleaned_data["event_date"]
        # Block ANY booking on the same date (new/review/accepted), excluding self when editing
        exists = BookingRequest.objects.filter(
            event_date=date, status__in=["new", "review", "accepted"]
        ).exclude(pk=self.instance.pk).exists()
        if exists:
            raise ValidationError("Sorry, that date is already booked. Please choose another.")
        return date
