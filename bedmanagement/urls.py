from django.urls import path

from . import views

app_name = "bedmanagement"

urlpatterns = [
    path("", views.bed_list, name="list"),
    path("create/", views.bed_create, name="create"),
    path("<int:pk>/edit/", views.bed_update, name="update"),
    path("<int:pk>/delete/", views.bed_delete, name="delete"),
]
