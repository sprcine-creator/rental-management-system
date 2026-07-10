from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from django.contrib import messages

from projects.models import Project

from .models import CommercialRate
from .forms import CommercialRateForm


def commercial_list(request, project_id):

    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    rates = CommercialRate.objects.filter(
        project=project
    ).select_related("equipment")

    return render(
        request,
        "commercials/list.html",
        {
            "project": project,
            "rates": rates,
        },
    )


def commercial_create(request, project_id):

    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":

        form = CommercialRateForm(request.POST)

        if form.is_valid():

            rate = form.save(commit=False)

            rate.project = project

            rate.save()

            messages.success(
                request,
                "Commercial rate added."
            )

            return redirect(
                "commercial_list",
                project_id=project.id,
            )

    else:

        form = CommercialRateForm()

    return render(
        request,
        "commercials/form.html",
        {
            "project": project,
            "form": form,
        },
    )