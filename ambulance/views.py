from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import AmbulanceForm
from .models import Ambulance


def ambulance_list(request):
    return render(request, "management/list.html", {"title": "Ambulances", "objects": Ambulance.objects.all(), "create_url": reverse("ambulance:create"), "update_url": "ambulance:update", "delete_url": "ambulance:delete"})


def ambulance_create(request):
    form = AmbulanceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ambulance saved.")
        return redirect("ambulance:list")
    return render(request, "management/form.html", {"title": "Add Ambulance", "form": form, "list_url": reverse("ambulance:list")})


def ambulance_update(request, pk):
    ambulance = get_object_or_404(Ambulance, pk=pk)
    form = AmbulanceForm(request.POST or None, instance=ambulance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ambulance updated.")
        return redirect("ambulance:list")
    return render(request, "management/form.html", {"title": "Edit Ambulance", "form": form, "list_url": reverse("ambulance:list")})


def ambulance_delete(request, pk):
    ambulance = get_object_or_404(Ambulance, pk=pk)
    if request.method == "POST":
        ambulance.delete()
        messages.success(request, "Ambulance deleted.")
        return redirect("ambulance:list")
    return render(request, "management/confirm_delete.html", {"title": "Ambulance", "object": ambulance, "list_url": reverse("ambulance:list")})
