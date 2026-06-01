from django.contrib import admin
from .models import LabReport


@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'patient', 'doctor', 'status', 'report_date']
    list_filter = ['status', 'report_date']
    search_fields = ['test_name', 'patient__full_name', 'doctor__user__username']
    readonly_fields = ['report_date']
    fieldsets = (
        ('Patient & Doctor', {
            'fields': ('patient', 'doctor')
        }),
        ('Test Information', {
            'fields': ('test_name', 'result')
        }),
        ('Status & Date', {
            'fields': ('status', 'report_date')
        }),
    )
