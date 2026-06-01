from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'location']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Department Information', {
            'fields': ('name', 'location', 'is_active')
        }),
        ('Description & Timestamps', {
            'fields': ('description', 'created_at')
        }),
    )
