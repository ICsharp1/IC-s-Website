from asyncio.windows_events import NULL
from pickle import NONE
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from register.models import Account
from .forms import sign_up_form
from .forms import adding_project_form
import os
# Create your views here.


def index(request):
    return render(request, 'main/base.html', {})


def bs(request):
    if request.user.is_authenticated:

        projects = Project.objects.filter(account=request.user.account)

        return render(request, 'main/bs.html', {"ps": projects, "count": len(projects)})
    return render(request, 'main/bs.html', {"ps": NULL, "count": NULL})


def split_list(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def home(request):
    ps = Project.objects.all()
    number_of_cards = 4
    ps = split_list(ps, number_of_cards)
    return render(request, 'main/home.html', {"ps": ps})


def projects(request):  # deprecated
    ps = Project.objects.all()
    number_of_cards = 4
    ps = split_list(ps, number_of_cards)
    return render(request, 'main/projects.html', {"ps": ps, "count": len(ps)})


def addproject(request):
    if request.user.is_authenticated:
        # print("\n\n\n\n\n\n", os.getcwd()) thats how you can print stuff that pretty cool
        if request.method == "POST":
            form = adding_project_form(request.POST)

            if form.is_valid():
                p = Project()
                p.account = request.user.account
                p.title = form.cleaned_data["title"]
                p.description = form.cleaned_data["description"]
                p.image = form.cleaned_data["image"]
                p.url = form.cleaned_data["url"]
                p.ProjectPageExists = form.cleaned_data["ProjectPageExists"]
                p.save()
                return redirect("/bs")
        else:
            form = adding_project_form()
        return render(request, 'main/addproject.html', {"form": form})
    return render(request, 'main/home.html', {})


def signup(request):
    if request.method == "POST":
        form = sign_up_form(request.POST)

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
    return render(request, 'main/signup.html', {"form": form})
