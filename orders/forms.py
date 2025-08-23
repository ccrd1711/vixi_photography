from django import forms
from django.utils import timezone
from .models import BookingRequest

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['event_date', 'location', 'details']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'placeholder': 'Additional Details', 'rows': 4}),
        }

    def clean_event_date(self):
        d = self.cleaned_data["event_date"]
        if d < timezone.localdate():
            raise forms.ValidationError("The event date cannot be in the past.")
        return d