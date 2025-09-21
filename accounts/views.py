from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from .models import Profile
from .forms import SignUpForm, ProfileForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data["password1"]
            user = authenticate
            (request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Account created. Welcome!")
                return redirect("gallery_index")
            messages.info(request, "Account created. Please log in.")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile, user=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})


@login_required
@require_http_methods(["GET", "POST"])
def account_delete(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been permanently deleted.")
        return redirect("home")
    return render(request, "accounts/account_confirm_delete.html")
