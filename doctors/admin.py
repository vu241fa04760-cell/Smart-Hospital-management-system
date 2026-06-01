from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'specialization', 'department', 'consultation_fee', 'is_available']
    list_filter = ['department', 'is_available', 'specialization']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'specialization']
    readonly_fields = []
    fieldsets = (
        ('User & Department', {
            'fields': ('user', 'department')
        }),
        ('Professional Details', {
            'fields': ('specialization', 'qualification', 'consultation_fee')
        }),
        ('Availability', {
            'fields': ('available_days', 'is_available', 'phone')
        }),
    )
    
    def get_name(self, obj):
        return obj.user.get_full_name() if obj.user else 'Doctor'
    get_name.short_description = 'Name'
