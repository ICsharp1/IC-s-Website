from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('addproject/', views.addproject, name='addproject'),
    path('projects', views.projects, name='projects'),
    path('bs', views.bs, name='bs'),
]
