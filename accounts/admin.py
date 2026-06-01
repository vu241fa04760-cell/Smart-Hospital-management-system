from django.contrib import admin
from .models import User, PatientProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "get_full_name",
        "role",
        "phone_number",
        "is_verified",
        "is_active",
        "created_at",
    ]
    list_filter = ["role", "is_verified", "is_active", "created_at"]
    search_fields = ["username", "email", "first_name", "last_name", "phone_number"]
    readonly_fields = ["created_at", "updated_at", "last_login", "date_joined"]
    
    fieldsets = (
        ("Personal Information", {
            "fields": ("username", "first_name", "last_name", "email", "phone_number", "profile_picture")
        }),
        ("Account Details", {
            "fields": ("role", "is_verified", "is_active", "is_staff", "is_superuser")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at", "date_joined", "last_login"),
            "classes": ("collapse",)
        }),
        ("Permissions", {
            "fields": ("groups", "user_permissions"),
            "classes": ("collapse",)
        }),
    )

    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username
    get_full_name.short_description = "Full Name"


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = [
        "patient_id",
        "get_user_name",
        "get_user_email",
        "age",
        "blood_group",
        "emergency_contact",
    ]
    list_filter = ["blood_group", "age"]
    search_fields = ["patient_id", "user__username", "user__email", "emergency_contact"]
    readonly_fields = ["patient_id"]
    
    fieldsets = (
        ("Patient Information", {
            "fields": ("patient_id", "user")
        }),
        ("Medical Details", {
            "fields": ("age", "blood_group", "medical_history")
        }),
        ("Contact Information", {
            "fields": ("address", "emergency_contact")
        }),
    )

    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_user_name.short_description = "User Name"

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = "Email"
