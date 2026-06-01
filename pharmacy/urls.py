from django.urls import path

from . import views

app_name = "pharmacy"

urlpatterns = [
    path("", views.medicine_list, name="list"),
    path("create/", views.medicine_create, name="create"),
    path("<int:pk>/edit/", views.medicine_update, name="update"),
    path("<int:pk>/delete/", views.medicine_delete, name="delete"),
]
