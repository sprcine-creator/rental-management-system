from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

def customer_list(request):

    search = request.GET.get("search", "")

    customers = Customer.objects.filter(
        is_active=True
    )

    if search:
        customers = customers.filter(
            name__icontains=search
        )

    customers = customers.order_by("name")

    return render(
        request,
        "customers/list.html",
        {
            "customers": customers,
            "search": search,
        },
   )


def customer_create(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Customer saved successfully."
            )

            return redirect("customer_list")

    else:

        form = CustomerForm()

    return render(
        request,
        "customers/form.html",
        {
            "form": form,
        },
    )


def customer_edit(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
            instance=customer,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Customer updated successfully."
            )

            return redirect("customer_list")

    else:

        form = CustomerForm(instance=customer)

    return render(
        request,
        "customers/form.html",
        {
            "form": form,
        },
    )

def customer_delete(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    customer.is_active = False
    customer.save()

    messages.success(
        request,
        "Customer archived successfully."
    )

    return redirect("customer_list")