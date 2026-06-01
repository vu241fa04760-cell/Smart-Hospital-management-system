from django.conf import settings
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, blank=True, null=True
    )
    specialization = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    available_days = models.CharField(max_length=120, help_text="Example: Mon, Wed, Fri")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        name = self.user.get_full_name() if self.user else "Doctor"
        return f"{name} - {self.specialization}"
