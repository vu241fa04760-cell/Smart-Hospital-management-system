from django.urls import path

from . import views

app_name = "appointment"

urlpatterns = [
    path("", views.appointment_list, name="list"),
    path("create/", views.appointment_create, name="create"),
    path("<int:pk>/edit/", views.appointment_update, name="update"),
    path("<int:pk>/delete/", views.appointment_delete, name="delete"),
]
