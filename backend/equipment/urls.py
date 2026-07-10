from django.urls import path
from . import views

urlpatterns = [
    path("", views.equipment_list, name="equipment_list"),

    path(
        "add/",
        views.equipment_create,
        name="equipment_create",
    ),
    path("edit/<int:pk>/", views.equipment_edit, name="equipment_edit"),
]