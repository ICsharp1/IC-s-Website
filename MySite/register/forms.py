from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registerForm(UserCreationForm):
    email = forms.EmailField()
    Dark = forms.BooleanField(
        label='DarkMode', required=False)

    class Meta:
        model = User
        exclude = ()
        # here i will add all fields and the checkbox for the dark mode
        fields = ['username', 'email', 'password1', 'password2', 'Dark']
