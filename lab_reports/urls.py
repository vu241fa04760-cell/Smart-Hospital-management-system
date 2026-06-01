from django.urls import path

from . import views

app_name = "lab_reports"

urlpatterns = [
    path("", views.lab_report_list, name="list"),
    path("create/", views.lab_report_create, name="create"),
    path("<int:pk>/edit/", views.lab_report_update, name="update"),
    path("<int:pk>/delete/", views.lab_report_delete, name="delete"),
]
