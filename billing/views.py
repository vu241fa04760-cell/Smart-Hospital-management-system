from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BillForm
from .models import Bill


def bill_list(request):
    return render(request, "management/list.html", {"title": "Bills", "objects": Bill.objects.all(), "create_url": reverse("billing:create"), "update_url": "billing:update", "delete_url": "billing:delete"})


def bill_create(request):
    form = BillForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bill saved.")
        return redirect("billing:list")
    return render(request, "management/form.html", {"title": "Add Bill", "form": form, "list_url": reverse("billing:list")})


def bill_update(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    form = BillForm(request.POST or None, instance=bill)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bill updated.")
        return redirect("billing:list")
    return render(request, "management/form.html", {"title": "Edit Bill", "form": form, "list_url": reverse("billing:list")})


def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == "POST":
        bill.delete()
        messages.success(request, "Bill deleted.")
        return redirect("billing:list")
    return render(request, "management/confirm_delete.html", {"title": "Bill", "object": bill, "list_url": reverse("billing:list")})
