from django.urls import path

from . import views

urlpatterns = [

    path(
        "<int:project_id>/",
        views.commercial_list,
        name="commercial_list",
    ),

    path(
        "<int:project_id>/add/",
        views.commercial_create,
        name="commercial_create",
    ),

]