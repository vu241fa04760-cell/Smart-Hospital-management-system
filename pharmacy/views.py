from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import MedicineForm
from .models import Medicine


def medicine_list(request):
    return render(request, "management/list.html", {"title": "Medicines", "objects": Medicine.objects.all(), "create_url": reverse("pharmacy:create"), "update_url": "pharmacy:update", "delete_url": "pharmacy:delete"})


def medicine_create(request):
    form = MedicineForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Medicine saved.")
        return redirect("pharmacy:list")
    return render(request, "management/form.html", {"title": "Add Medicine", "form": form, "list_url": reverse("pharmacy:list")})


def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.POST or None, instance=medicine)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Medicine updated.")
        return redirect("pharmacy:list")
    return render(request, "management/form.html", {"title": "Edit Medicine", "form": form, "list_url": reverse("pharmacy:list")})


def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        medicine.delete()
        messages.success(request, "Medicine deleted.")
        return redirect("pharmacy:list")
    return render(request, "management/confirm_delete.html", {"title": "Medicine", "object": medicine, "list_url": reverse("pharmacy:list")})
