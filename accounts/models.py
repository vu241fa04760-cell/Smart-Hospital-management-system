
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        ADMIN = "ADMIN", "Admin"
        NURSE = "NURSE", "Nurse"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=Roles.choices, default=Roles.PATIENT)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_admin_role(self):
        return self.role in [self.Roles.ADMIN, self.Roles.SUPER_ADMIN] or self.is_superuser

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_profile"
    )
    patient_id = models.CharField(max_length=20, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True)
    address = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.patient_id}"

