from asyncio.windows_events import NULL
from pickle import NONE
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import sign_up_form
from .forms import adding_project_form
# Create your views here.


def index(response):
    return render(response, 'main/base.html', {})


def bs(response):
    if response.user.is_authenticated:
        ps = response.user.projects.all()
        return render(response, 'main/bs.html', {"ps": ps, "count": len(ps)})
    return render(response, 'main/bs.html', {"ps": NULL, "count": NULL})


def profile(response):
    if response.user.is_authenticated:
        user = response.user
        return render(response, 'main/profile.html', {"user": user})
    return render(response, 'main/home.html', {})


def split_list(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def home(response):
    ps = Project.objects.all()
    number_of_cards = 4
    ps = split_list(ps, number_of_cards)
    return render(response, 'main/home.html', {"ps": ps})


def projects(response):
    ps = Project.objects.all()
    number_of_cards = 4
    ps = split_list(ps, number_of_cards)
    return render(response, 'main/projects.html', {"ps": ps, "count": len(ps)})


def addproject(response):
    if response.method == "POST":
        form = adding_project_form(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            url = form.cleaned_data["url"]
            ProjectPageExists = form.cleaned_data["ProjectPageExists"]
            p = Project(title=title, description=description, image=image,
                        url=url, ProjectPageExists=ProjectPageExists)
            p.save()
            if response.user.projects.all().count() <= 100:
                response.user.projects.add(p)
            return redirect('/projects')

    else:
        form = adding_project_form()
    return render(response, 'main/addproject.html', {"form": form})


def signup(response):
    if response.method == "POST":
        form = sign_up_form(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            url = form.cleaned_data["url"]
            ProjectPageExists = form.cleaned_data["ProjectPageExists"]
            p = Project(title=title, description=description, image=image,
                        url=url, ProjectPageExists=ProjectPageExists)
            p.save()
    else:
        form = sign_up_form()
    return render(response, 'main/signup.html', {"form": form})
