from django.urls import path

from . import views

app_name = "prescriptions"

urlpatterns = [
    path("", views.prescription_list, name="list"),
    path("create/", views.prescription_create, name="create"),
    path("<int:pk>/edit/", views.prescription_update, name="update"),
    path("<int:pk>/delete/", views.prescription_delete, name="delete"),
]
