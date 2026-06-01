from django.urls import path

from . import views

app_name = "hospitaltiming"

urlpatterns = [
    path("", views.timing_list, name="list"),
    path("create/", views.timing_create, name="create"),
    path("<int:pk>/edit/", views.timing_update, name="update"),
    path("<int:pk>/delete/", views.timing_delete, name="delete"),
]
