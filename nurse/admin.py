from django.contrib import admin
from .models import Nurse


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'department', 'shift', 'phone', 'is_active']
    list_filter = ['department', 'shift', 'is_active']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone']
    fieldsets = (
        ('User & Department', {
            'fields': ('user', 'department')
        }),
        ('Work Details', {
            'fields': ('shift', 'is_active')
        }),
        ('Contact', {
            'fields': ('phone',)
        }),
    )
    
    def get_name(self, obj):
        return obj.user.get_full_name() if obj.user else f'Nurse {obj.id}'
    get_name.short_description = 'Name'
