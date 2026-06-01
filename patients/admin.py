from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'full_name', 'age', 'gender', 'blood_group', 'phone', 'registered_at']
    list_filter = ['gender', 'blood_group', 'registered_at']
    search_fields = ['patient_id', 'full_name', 'phone']
    readonly_fields = ['registered_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('patient_id', 'full_name', 'age', 'gender', 'blood_group', 'phone')
        }),
        ('Address & History', {
            'fields': ('address', 'medical_history')
        }),
        ('User & Timestamps', {
            'fields': ('user', 'registered_at'),
            'classes': ('collapse',)
        }),
    )
