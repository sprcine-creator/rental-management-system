from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("equipment/", include("equipment.urls")),

    path("customers/", include("customers.urls")),

    path("projects/", include("projects.urls")),
]