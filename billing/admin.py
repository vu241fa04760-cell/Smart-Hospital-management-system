from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_number', 'patient', 'total_amount', 'paid_amount', 'status', 'issued_on']
    list_filter = ['status', 'issued_on']
    search_fields = ['bill_number', 'patient__full_name']
    readonly_fields = ['issued_on']
    fieldsets = (
        ('Bill Information', {
            'fields': ('bill_number', 'patient', 'appointment')
        }),
        ('Amount & Status', {
            'fields': ('total_amount', 'paid_amount', 'status')
        }),
        ('Description & Date', {
            'fields': ('description', 'issued_on')
        }),
    )
