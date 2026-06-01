from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import StaffForm
from .models import Staff


def staff_list(request):
    return render(request, "management/list.html", {"title": "Staff", "objects": Staff.objects.all(), "create_url": reverse("staff:create"), "update_url": "staff:update", "delete_url": "staff:delete"})


def staff_create(request):
    form = StaffForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Staff member saved.")
        return redirect("staff:list")
    return render(request, "management/form.html", {"title": "Add Staff", "form": form, "list_url": reverse("staff:list")})


def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    form = StaffForm(request.POST or None, instance=staff)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Staff member updated.")
        return redirect("staff:list")
    return render(request, "management/form.html", {"title": "Edit Staff", "form": form, "list_url": reverse("staff:list")})


def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        staff.delete()
        messages.success(request, "Staff member deleted.")
        return redirect("staff:list")
    return render(request, "management/confirm_delete.html", {"title": "Staff", "object": staff, "list_url": reverse("staff:list")})
