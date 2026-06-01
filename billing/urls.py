from django.urls import path

from . import views

app_name = "billing"

urlpatterns = [
    path("", views.bill_list, name="list"),
    path("create/", views.bill_create, name="create"),
    path("<int:pk>/edit/", views.bill_update, name="update"),
    path("<int:pk>/delete/", views.bill_delete, name="delete"),
]
