from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import NurseForm
from .models import Nurse


def nurse_list(request):
    return render(request, "management/list.html", {"title": "Nurses", "objects": Nurse.objects.all(), "create_url": reverse("nurse:create"), "update_url": "nurse:update", "delete_url": "nurse:delete"})


def nurse_create(request):
    form = NurseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Nurse saved.")
        return redirect("nurse:list")
    return render(request, "management/form.html", {"title": "Add Nurse", "form": form, "list_url": reverse("nurse:list")})


def nurse_update(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    form = NurseForm(request.POST or None, instance=nurse)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Nurse updated.")
        return redirect("nurse:list")
    return render(request, "management/form.html", {"title": "Edit Nurse", "form": form, "list_url": reverse("nurse:list")})


def nurse_delete(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    if request.method == "POST":
        nurse.delete()
        messages.success(request, "Nurse deleted.")
        return redirect("nurse:list")
    return render(request, "management/confirm_delete.html", {"title": "Nurse", "object": nurse, "list_url": reverse("nurse:list")})
