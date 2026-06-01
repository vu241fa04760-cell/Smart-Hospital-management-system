from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import DepartmentForm
from .models import Department


def department_list(request):
    return render(request, "management/list.html", {
        "title": "Departments",
        "objects": Department.objects.all(),
        "create_url": reverse("departments:create"),
        "update_url": "departments:update",
        "delete_url": "departments:delete",
    })


def department_create(request):
    form = DepartmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Department saved.")
        return redirect("departments:list")
    return render(request, "management/form.html", {"title": "Add Department", "form": form, "list_url": reverse("departments:list")})


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Department updated.")
        return redirect("departments:list")
    return render(request, "management/form.html", {"title": "Edit Department", "form": form, "list_url": reverse("departments:list")})


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        messages.success(request, "Department deleted.")
        return redirect("departments:list")
    return render(request, "management/confirm_delete.html", {"title": "Department", "object": department, "list_url": reverse("departments:list")})
