from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PrescriptionForm
from .models import Prescription


def prescription_list(request):
    return render(request, "management/list.html", {"title": "Prescriptions", "objects": Prescription.objects.all(), "create_url": reverse("prescriptions:create"), "update_url": "prescriptions:update", "delete_url": "prescriptions:delete"})


def prescription_create(request):
    form = PrescriptionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Prescription saved.")
        return redirect("prescriptions:list")
    return render(request, "management/form.html", {"title": "Add Prescription", "form": form, "list_url": reverse("prescriptions:list")})


def prescription_update(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    form = PrescriptionForm(request.POST or None, instance=prescription)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Prescription updated.")
        return redirect("prescriptions:list")
    return render(request, "management/form.html", {"title": "Edit Prescription", "form": form, "list_url": reverse("prescriptions:list")})


def prescription_delete(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == "POST":
        prescription.delete()
        messages.success(request, "Prescription deleted.")
        return redirect("prescriptions:list")
    return render(request, "management/confirm_delete.html", {"title": "Prescription", "object": prescription, "list_url": reverse("prescriptions:list")})
