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
    user = request.user
    if user.is_authenticated:
        dark = user.account.Dark
        projects = Project.objects.filter(account=request.user.account)

        return render(request, 'main/bs.html', {"ps": projects, "count": len(projects), "id": "Browse", "Dark": dark})
    return home(request, 'You need to sign in order to watch your projects')


def projectId(request, pk):
    user = request.user
    if user.is_authenticated:
        dark = user.account.Dark
        p = Project.objects.get(id=pk)
        print("\n\n\n\n\n\n", os.getcwd())
        print(p, os.getcwd())
        print("\n\n\n\n\n\n", os.getcwd())
        project_creator = p.account
        account = user.account
        if account == project_creator:
            return render(request, 'main/project.html', {"p": p, "Dark": dark})
        else:
            home(request, 'You can\'t view a project that is not your\'s')


def split_list(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def home(request, alert='~~'):
    user = request.user
    if user.is_authenticated:
        dark = user.account.Dark
        if alert != '~~':
            return render(request, 'main/home.html', {"alert": alert, "id": "home", "Dark": dark})
        else:
            return render(request, 'main/home.html', {"alert": alert, "id": "home", "Dark": dark})
    else:
        return render(request, 'main/home.html', {"alert": alert, "id": "home", "Dark": NULL})


def projects(request):  # deprecated
    ps = Project.objects.all()
    number_of_cards = 4
    ps = split_list(ps, number_of_cards)
    return render(request, 'main/projects.html', {"ps": ps, "count": len(ps)})


def addproject(request):
    user = request.user
    if user.is_authenticated:
        dark = user.account.Dark
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
                return home(request, "You project was successfully added to your collection")
        else:
            form = adding_project_form()
            return render(request, 'main/addproject.html', {"form": form, "id": "Add", "Dark": dark})

    return home(request, 'You need to sign in order to Add a project')
