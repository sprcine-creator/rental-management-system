from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipment = Equipment.objects.filter(
        is_active=True
    ).order_by("name")

    return render(
        request,
        "equipment/list.html",
        {
            "equipment": equipment
        }
    )


def equipment_create(request):

    if request.method == "POST":

        form = EquipmentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("equipment_list")

    else:

        form = EquipmentForm()

    return render(
        request,
        "equipment/form.html",
        {
            "form": form
        }
    )




def equipment_edit(request, pk):

    equipment = get_object_or_404(Equipment, pk=pk)

    if request.method == "POST":

        form = EquipmentForm(request.POST, instance=equipment)

        if form.is_valid():
            form.save()

            return redirect("equipment_list")

    else:

        form = EquipmentForm(instance=equipment)

    return render(
        request,
        "equipment/form.html",
        {
            "form": form,
        },
    )