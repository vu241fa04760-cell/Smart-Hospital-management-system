from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'manufacturer', 'stock_quantity', 'price', 'expiry_date']
    list_filter = ['category', 'expiry_date', 'manufacturer']
    search_fields = ['name', 'category', 'manufacturer']
    fieldsets = (
        ('Medicine Information', {
            'fields': ('name', 'category', 'manufacturer')
        }),
        ('Stock & Price', {
            'fields': ('stock_quantity', 'price')
        }),
        ('Expiry Date', {
            'fields': ('expiry_date',)
        }),
    )
