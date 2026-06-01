from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'designation', 'department', 'phone', 'joining_date', 'is_active']
    list_filter = ['department', 'is_active', 'joining_date']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'designation', 'phone']
    fieldsets = (
        ('User & Department', {
            'fields': ('user', 'department')
        }),
        ('Job Details', {
            'fields': ('designation', 'joining_date', 'is_active')
        }),
        ('Contact', {
            'fields': ('phone',)
        }),
    )
    
    def get_name(self, obj):
        return obj.user.get_full_name() if obj.user else 'Staff'
    get_name.short_description = 'Name'
