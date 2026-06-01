from django.urls import path

from . import views

app_name = "doctors"

urlpatterns = [
    path("", views.doctor_list, name="list"),
    path("create/", views.doctor_create, name="create"),
    path("<int:pk>/edit/", views.doctor_update, name="update"),
    path("<int:pk>/delete/", views.doctor_delete, name="delete"),
]
