from django import forms
from django.forms import ModelForm
from .models import Project, Comment
from register.models import Account


class sign_up_form(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=254, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirm Password')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError('Password does not match')
    #     return cleaned_data


class log_in_form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


# class adding_project_form(forms.Form):
#     title = forms.CharField(max_length=200, label='Title')
#     description = forms.CharField(label='Description', widget=forms.Textarea)
#     image = forms.URLField(label='Image Link')
#     url = forms.URLField(label='Project Link')
#     ProjectPageExists = forms.BooleanField(
#         label='Project Page Exists', required=False)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError('Password does not match')
    #     return cleaned_data


class adding_project_form(ModelForm):
    title = forms.CharField(max_length=200, label='Title')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.URLField(label='Image Link')
    url = forms.URLField(label='Project Link', required=False)
    ProjectPageExists = forms.BooleanField(
        label='Project Page Exists', required=False)

    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url', 'ProjectPageExists']


class adding_comment_form(ModelForm):
    commentText = forms.CharField(label='Comment', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['commentText']


class dark_mode(ModelForm):
    pass
