from django.shortcuts import render, redirect
from .forms import registerForm
from MyApp.views import home
from .models import Account
import os
from MyApp import views


def register(request):
    if request.method == "POST":
        user_form = registerForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return home(request, 'Your account was successfully created')

    else:
        user_form = registerForm()
    return render(request, "register/register.html", {"user_form": user_form, "id": "Register"})


def profile(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            account_form = registerForm(
                request.POST, instance=request.user.Account)

            if (account_form.is_valid()):
                account_form.save()
                return home(request, 'Your account was updated successfully')
            return home(request, 'Form was not valid')

        else:
            account_form = registerForm(instance=user.account)
            return render(request, "profile.html", {"user_form": account_form, "id": "Profile"})
    else:
        return home(request, 'You need to sign in first')

# i need to add a grid of fire particles - mostly using javascript
