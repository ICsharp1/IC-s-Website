from django import forms
from django.forms import ModelForm
from .models import Project, Comment
from register.models import Account


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
