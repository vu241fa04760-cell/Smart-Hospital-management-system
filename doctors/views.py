from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import DoctorForm
from .models import Doctor


def doctor_list(request):
    return render(request, "management/list.html", {"title": "Doctors", "objects": Doctor.objects.all(), "create_url": reverse("doctors:create"), "update_url": "doctors:update", "delete_url": "doctors:delete"})


def doctor_create(request):
    form = DoctorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Doctor saved.")
        return redirect("doctors:list")
    return render(request, "management/form.html", {"title": "Add Doctor", "form": form, "list_url": reverse("doctors:list")})


def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Doctor updated.")
        return redirect("doctors:list")
    return render(request, "management/form.html", {"title": "Edit Doctor", "form": form, "list_url": reverse("doctors:list")})


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        messages.success(request, "Doctor deleted.")
        return redirect("doctors:list")
    return render(request, "management/confirm_delete.html", {"title": "Doctor", "object": doctor, "list_url": reverse("doctors:list")})
