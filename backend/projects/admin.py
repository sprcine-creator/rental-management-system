from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_name",
        "customer",
        "project_type",
        "status",
        "start_date",
    )

    list_filter = (
        "status",
        "project_type",
    )

    search_fields = (
        "project_name",
        "customer__name",
    )