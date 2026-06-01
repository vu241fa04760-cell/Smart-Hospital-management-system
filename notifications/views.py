from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import NotificationForm
from .models import Notification


def notification_list(request):
    return render(request, "management/list.html", {"title": "Notifications", "objects": Notification.objects.all(), "create_url": reverse("notifications:create"), "update_url": "notifications:update", "delete_url": "notifications:delete"})


def notification_create(request):
    form = NotificationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Notification saved.")
        return redirect("notifications:list")
    return render(request, "management/form.html", {"title": "Add Notification", "form": form, "list_url": reverse("notifications:list")})


def notification_update(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    form = NotificationForm(request.POST or None, instance=notification)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Notification updated.")
        return redirect("notifications:list")
    return render(request, "management/form.html", {"title": "Edit Notification", "form": form, "list_url": reverse("notifications:list")})


def notification_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == "POST":
        notification.delete()
        messages.success(request, "Notification deleted.")
        return redirect("notifications:list")
    return render(request, "management/confirm_delete.html", {"title": "Notification", "object": notification, "list_url": reverse("notifications:list")})
