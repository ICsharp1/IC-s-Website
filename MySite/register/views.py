from django.shortcuts import render, redirect
from .forms import registerForm
#from django.contrib.auth.forms import UserCreationForm
from .models import Account
import os
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
    return render(request, "register/register.html", {"user_form": user_form})


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {"user": user})
    return render(request, 'main/home.html', {})
