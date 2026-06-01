from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BedForm
from .models import Bed


def bed_list(request):
    return render(request, "management/list.html", {"title": "Beds", "objects": Bed.objects.all(), "create_url": reverse("bedmanagement:create"), "update_url": "bedmanagement:update", "delete_url": "bedmanagement:delete"})


def bed_create(request):
    form = BedForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bed saved.")
        return redirect("bedmanagement:list")
    return render(request, "management/form.html", {"title": "Add Bed", "form": form, "list_url": reverse("bedmanagement:list")})


def bed_update(request, pk):
    bed = get_object_or_404(Bed, pk=pk)
    form = BedForm(request.POST or None, instance=bed)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bed updated.")
        return redirect("bedmanagement:list")
    return render(request, "management/form.html", {"title": "Edit Bed", "form": form, "list_url": reverse("bedmanagement:list")})


def bed_delete(request, pk):
    bed = get_object_or_404(Bed, pk=pk)
    if request.method == "POST":
        bed.delete()
        messages.success(request, "Bed deleted.")
        return redirect("bedmanagement:list")
    return render(request, "management/confirm_delete.html", {"title": "Bed", "object": bed, "list_url": reverse("bedmanagement:list")})
