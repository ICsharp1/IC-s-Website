from email.policy import default
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account


class registerForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    Dark = forms.BooleanField(label='DarkMode', required=False)

    class Meta:
        model = User
        exclude = ()
        fields = ['username', 'email', 'password1', 'password2', 'Dark']

    def save(self):
        user = super(registerForm, self).save(commit=True)
        user_profile = Account(
            user=user, Dark=self.cleaned_data['Dark'], email=self.cleaned_data['email'])
        user_profile.save()
        return user, user_profile


# class UpdateAccountForm(forms.ModelForm):
#     email = forms.EmailField(max_length=200, help_text='Required')r
#     Dark = forms.BooleanField(label='DarkMode', required=False)

#     class Meta:r
#         model = Account
#         fields = ['username', 'email', 'password1', 'password2', 'Dark']

#     def save(self):
#         user = super(registerForm, self).save(commit=True)
#         user_profile = Account(
#             user=user, Dark=self.cleaned_data['Dark'], email=self.cleaned_data['email'])
#         user_profile.save()
#         return user, user_profile
