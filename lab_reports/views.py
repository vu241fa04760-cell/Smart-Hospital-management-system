from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import LabReportForm
from .models import LabReport


def lab_report_list(request):
    return render(request, "management/list.html", {"title": "Lab Reports", "objects": LabReport.objects.all(), "create_url": reverse("lab_reports:create"), "update_url": "lab_reports:update", "delete_url": "lab_reports:delete"})


def lab_report_create(request):
    form = LabReportForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lab report saved.")
        return redirect("lab_reports:list")
    return render(request, "management/form.html", {"title": "Add Lab Report", "form": form, "list_url": reverse("lab_reports:list")})


def lab_report_update(request, pk):
    report = get_object_or_404(LabReport, pk=pk)
    form = LabReportForm(request.POST or None, instance=report)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lab report updated.")
        return redirect("lab_reports:list")
    return render(request, "management/form.html", {"title": "Edit Lab Report", "form": form, "list_url": reverse("lab_reports:list")})


def lab_report_delete(request, pk):
    report = get_object_or_404(LabReport, pk=pk)
    if request.method == "POST":
        report.delete()
        messages.success(request, "Lab report deleted.")
        return redirect("lab_reports:list")
    return render(request, "management/confirm_delete.html", {"title": "Lab Report", "object": report, "list_url": reverse("lab_reports:list")})
