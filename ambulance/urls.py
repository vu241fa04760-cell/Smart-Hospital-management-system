from django.urls import path

from . import views

app_name = "ambulance"

urlpatterns = [
    path("", views.ambulance_list, name="list"),
    path("create/", views.ambulance_create, name="create"),
    path("<int:pk>/edit/", views.ambulance_update, name="update"),
    path("<int:pk>/delete/", views.ambulance_delete, name="delete"),
]
