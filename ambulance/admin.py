from django.contrib import admin
from .models import Ambulance


@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ['vehicle_number', 'driver_name', 'driver_phone', 'current_location', 'status']
    list_filter = ['status']
    search_fields = ['vehicle_number', 'driver_name', 'driver_phone']
    fieldsets = (
        ('Vehicle Information', {
            'fields': ('vehicle_number', 'status')
        }),
        ('Driver Details', {
            'fields': ('driver_name', 'driver_phone')
        }),
        ('Location', {
            'fields': ('current_location',)
        }),
    )
