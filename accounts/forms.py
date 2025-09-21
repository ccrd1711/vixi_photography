from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="We'll send confirmations here."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    # accept `user` kwarg from the view, even if we don't use it now
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ("display_name", "address", "phone")
        widgets = {
            "display_name": forms.TextInput(attrs={"placeholder": "Name"}),
            "address": forms.Textarea(attrs={"rows": 3, "placeholder":
                                             "Address"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
        }
