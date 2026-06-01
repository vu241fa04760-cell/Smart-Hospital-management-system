from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'department', 'appointment_date', 'status', 'created_at']
    list_filter = ['status', 'appointment_date', 'department']
    search_fields = ['patient__full_name', 'doctor__user__username']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Appointment Details', {
            'fields': ('patient', 'doctor', 'department', 'appointment_date')
        }),
        ('Status & Notes', {
            'fields': ('status', 'reason')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
