from django.contrib import admin
from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'prescribed_on']
    list_filter = ['prescribed_on']
    search_fields = ['patient__full_name', 'doctor__user__username', 'medicines']
    readonly_fields = ['prescribed_on']
    fieldsets = (
        ('Patient & Doctor', {
            'fields': ('patient', 'doctor')
        }),
        ('Medicines & Notes', {
            'fields': ('medicines', 'notes')
        }),
        ('Date', {
            'fields': ('prescribed_on',),
            'classes': ('collapse',)
        }),
    )
