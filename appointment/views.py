from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import AppointmentForm
from .models import Appointment


def appointment_list(request):
    return render(request, "management/list.html", {"title": "Appointments", "objects": Appointment.objects.all(), "create_url": reverse("appointment:create"), "update_url": "appointment:update", "delete_url": "appointment:delete"})


def appointment_create(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Appointment saved.")
        return redirect("appointment:list")
    return render(request, "management/form.html", {"title": "Add Appointment", "form": form, "list_url": reverse("appointment:list")})


def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Appointment updated.")
        return redirect("appointment:list")
    return render(request, "management/form.html", {"title": "Edit Appointment", "form": form, "list_url": reverse("appointment:list")})


def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Appointment deleted.")
        return redirect("appointment:list")
    return render(request, "management/confirm_delete.html", {"title": "Appointment", "object": appointment, "list_url": reverse("appointment:list")})
