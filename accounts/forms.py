from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["display_name", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }

