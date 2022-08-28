from email.policy import default
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Account


class registerForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    Dark = forms.BooleanField(label='DarkMode', required=False)

    class Meta:
        model = User
        exclude = ()
        # here i will add all fields and the checkbox for the dark mode
        fields = ['username', 'email', 'password1', 'password2', 'Dark']

    def save(self):
        user = super(registerForm, self).save(commit=True)
        user_profile = Account(
            user=user, Dark=self.cleaned_data['Dark'], email=self.cleaned_data['email'])
        user_profile.save()
        return user, user_profile


# class AccountForm(UserCreationForm):
#     Dark = forms.BooleanField(
#         label='DarkMode')

#     class Meta:
#         model = Account
#         exclude = ('password1', 'password2')
#         # here i will add all fields and the checkbox for the dark mode
#         fields = ['Dark']
