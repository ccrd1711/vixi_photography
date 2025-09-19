from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from .models import BookingRequest

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ["event_date", "location", "details"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date", "min": date.today().isoformat()}),
            "location": forms.TextInput(attrs={"pattern": r".*[A-Za-z].*", "inputmode": "text"}),
        }

    def clean_event_date(self):
        d = self.cleaned_data["event_date"]
        if d < date.today():
            raise ValidationError("Please choose a date in the future.")
        exists = BookingRequest.objects.filter(
            event_date=d, status__in=["new", "review", "accepted"]
        ).exclude(pk=self.instance.pk).exists()
        if exists:
            raise ValidationError("Sorry, that date is already booked. Please choose another.")
        return d

    def clean_location(self):
        loc = (self.cleaned_data.get("location") or "").strip()
        if not any(ch.isalpha() for ch in loc):
            raise ValidationError("Location must include letters (not just numbers).")
        if len(loc) < 3:
            raise ValidationError("Location must be at least 3 characters.")
        return loc
