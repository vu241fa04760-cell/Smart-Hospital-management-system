"""
URL configuration for hospitalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
from admin_custom.admin_site import custom_admin_site

urlpatterns = [
    path('', account_views.home, name='home'),
    path('admin/', custom_admin_site.urls),
    path('accounts/', include('accounts.urls')),
    path('ambulance/', include('ambulance.urls')),
    path('appointments/', include('appointment.urls')),
    path('beds/', include('bedmanagement.urls')),
    path('billing/', include('billing.urls')),
    path('departments/', include('departments.urls')),
    path('doctors/', include('doctors.urls')),
    path('hospital-timings/', include('hospitaltiming.urls')),
    path('lab-reports/', include('lab_reports.urls')),
    path('notifications/', include('notifications.urls')),
    path('nurses/', include('nurse.urls')),
    path('patients/', include('patients.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('staff/', include('staff.urls')),
]

# Serve uploaded files and project static assets in development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
