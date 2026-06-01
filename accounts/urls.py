from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.accounts_home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("dashboard/", views.dashboard_redirect, name="dashboard"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path("users/", views.user_list, name="user_list"),
    path("users/create/", views.user_create, name="user_create"),
    path("users/<int:pk>/edit/", views.user_update, name="user_update"),
    path("users/<int:pk>/delete/", views.user_delete, name="user_delete"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/create/", views.patient_create, name="patient_create"),
    path("patients/<int:pk>/edit/", views.patient_update, name="patient_update"),
    path("patients/<int:pk>/delete/", views.patient_delete, name="patient_delete"),
]

