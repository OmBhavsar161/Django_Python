from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name="app_home"),
    path("projects/", views.app_projects, name="app_projects")
]