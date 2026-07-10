from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("add/", views.project_create, name="project_create"),
    path("edit/<int:pk>/", views.project_edit, name="project_edit"),
    path(
    "<int:pk>/", views.project_workspace, name="project_workspace",),
]