from django.contrib import admin
from django.urls import path, include
from register import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    #path('profile/', TemplateView.as_view(template_name="about.html")),
]
