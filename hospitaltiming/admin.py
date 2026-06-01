from django.contrib import admin
from .models import HospitalTiming


@admin.register(HospitalTiming)
class HospitalTimingAdmin(admin.ModelAdmin):
    list_display = ['department', 'day_of_week', 'opening_time', 'closing_time', 'is_closed']
    list_filter = ['day_of_week', 'is_closed', 'department']
    search_fields = ['department__name', 'day_of_week']
    fieldsets = (
        ('Department & Day', {
            'fields': ('department', 'day_of_week')
        }),
        ('Timing & Status', {
            'fields': ('opening_time', 'closing_time', 'is_closed')
        }),
    )
