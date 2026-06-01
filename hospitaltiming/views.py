from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import HospitalTimingForm
from .models import HospitalTiming


def timing_list(request):
    return render(request, "management/list.html", {"title": "Hospital Timings", "objects": HospitalTiming.objects.all(), "create_url": reverse("hospitaltiming:create"), "update_url": "hospitaltiming:update", "delete_url": "hospitaltiming:delete"})


def timing_create(request):
    form = HospitalTimingForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Timing saved.")
        return redirect("hospitaltiming:list")
    return render(request, "management/form.html", {"title": "Add Timing", "form": form, "list_url": reverse("hospitaltiming:list")})


def timing_update(request, pk):
    timing = get_object_or_404(HospitalTiming, pk=pk)
    form = HospitalTimingForm(request.POST or None, instance=timing)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Timing updated.")
        return redirect("hospitaltiming:list")
    return render(request, "management/form.html", {"title": "Edit Timing", "form": form, "list_url": reverse("hospitaltiming:list")})


def timing_delete(request, pk):
    timing = get_object_or_404(HospitalTiming, pk=pk)
    if request.method == "POST":
        timing.delete()
        messages.success(request, "Timing deleted.")
        return redirect("hospitaltiming:list")
    return render(request, "management/confirm_delete.html", {"title": "Timing", "object": timing, "list_url": reverse("hospitaltiming:list")})
