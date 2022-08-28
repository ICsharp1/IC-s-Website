from django.shortcuts import render, redirect
from .forms import registerForm
#from django.contrib.auth.forms import UserCreationForm
from .models import Account
import os
from MyApp import views
# Create your views here.


# class profileView(templateView):
#     template_name = "profile.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         return context


def register(request):
    if request.method == "POST":
        user_form = registerForm(request.POST)
        #form = AccountForm(request.POST)
        # and form.is_valid()
        if user_form.is_valid():
            user = user_form.save()
            #Account = form.save(commit=False)
            #Account.user = user
            # Account.save()
            return redirect("/")

    else:
        user_form = registerForm()
        #form = AccountForm()
    return render(request, "register/register.html", {"user_form": user_form, "id": "Register"})


def profile(request):
    user = request.user
    if request.user.is_authenticated:
        dark = user.account.Dark
        return render(request, 'profile.html', {"user": user, "id": "Profile"})
    return views.home(request, 'You need to sign in order to see your profile')


# i need to add a grid of fire particles - mostly using javascript
