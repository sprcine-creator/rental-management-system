from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Project
from .forms import ProjectForm


def project_list(request):

    search = request.GET.get("search", "")

    projects = Project.objects.select_related("customer")

    if search:
        projects = projects.filter(
            project_name__icontains=search
        )

    projects = projects.order_by("project_name")

    return render(
        request,
        "projects/list.html",
        {
            "projects": projects,
            "search": search,
        },
    )


def project_create(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project created successfully."
            )

            return redirect("project_list")

    else:

        form = ProjectForm()

    return render(
        request,
        "projects/form.html",
        {
            "form": form,
        },
    )


def project_edit(request, pk):

    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            instance=project,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project updated successfully."
            )

            return redirect("project_list")

    else:

        form = ProjectForm(
            instance=project,
        )

    return render(
        request,
        "projects/form.html",
        {
            "form": form,
        },
    )

def project_workspace(request, pk):

    project = get_object_or_404(
        Project.objects.select_related("customer"),
        pk=pk,
    )

    return render(
        request,
        "projects/workspace.html",
        {
            "project": project,
        },
    )