from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PatientForm
from .models import Patient


def patient_list(request):
    return render(request, "management/list.html", {"title": "Patients", "objects": Patient.objects.all(), "create_url": reverse("patients:create"), "update_url": "patients:update", "delete_url": "patients:delete"})


def patient_create(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient saved.")
        return redirect("patients:list")
    return render(request, "management/form.html", {"title": "Add Patient", "form": form, "list_url": reverse("patients:list")})


def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient updated.")
        return redirect("patients:list")
    return render(request, "management/form.html", {"title": "Edit Patient", "form": form, "list_url": reverse("patients:list")})


def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        messages.success(request, "Patient deleted.")
        return redirect("patients:list")
    return render(request, "management/confirm_delete.html", {"title": "Patient", "object": patient, "list_url": reverse("patients:list")})
