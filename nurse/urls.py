from django.urls import path

from . import views

app_name = "nurse"

urlpatterns = [
    path("", views.nurse_list, name="list"),
    path("create/", views.nurse_create, name="create"),
    path("<int:pk>/edit/", views.nurse_update, name="update"),
    path("<int:pk>/delete/", views.nurse_delete, name="delete"),
]
