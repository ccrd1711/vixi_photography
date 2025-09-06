from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="We’ll send confirmations here.")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
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
    # show user.email read-only in the form
    email = forms.EmailField(disabled=True, required=False, label="Email")

    class Meta:
        model = Profile
        fields = ["display_name", "phone", "address"]  # no email here

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["email"].initial = user.email
