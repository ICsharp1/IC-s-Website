from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import sign_up_form
from .forms import adding_project_form
# Create your views here.


def index(response):
    return render(response, 'base.html', {})


def home(response):
    ps = Project.objects.all()
    return render(response, 'main/home.html', {"ps": ps})


def addproject(response):
    if response.method == "POST":
        form = adding_project_form(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            imageLink = form.cleaned_data["imageLink"]
            Projectlink = form.cleaned_data["Projectlink"]
            ProjectPageExists = form.cleaned_data["ProjectPageExists"]
            p = Project(title=title, description=description, imageLink=imageLink,
                        Projectlink=Projectlink, ProjectPageExists=ProjectPageExists)
            p.save()
    else:
        form = adding_project_form()
    return render(response, 'main/addproject.html', {"form": form})


def signup(response):
    if response.method == "POST":
        form = sign_up_form(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            imageLink = form.cleaned_data["imageLink"]
            Projectlink = form.cleaned_data["Projectlink"]
            ProjectPageExists = form.cleaned_data["ProjectPageExists"]
            p = Project(title=title, description=description, imageLink=imageLink,
                        Projectlink=Projectlink, ProjectPageExists=ProjectPageExists)
            p.save()
    else:
        form = sign_up_form()
    return render(response, 'main/signup.html', {"form": form})
