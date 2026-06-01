from django.contrib import admin
from .models import Bed


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'ward', 'bed_type', 'status', 'patient']
    list_filter = ['bed_type', 'status', 'ward']
    search_fields = ['bed_number', 'ward', 'patient__full_name']
    fieldsets = (
        ('Bed Information', {
            'fields': ('bed_number', 'ward', 'bed_type')
        }),
        ('Status & Patient', {
            'fields': ('status', 'patient')
        }),
    )
