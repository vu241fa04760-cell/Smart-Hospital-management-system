from django.conf import settings
from django.db import models


class Nurse(models.Model):
    class Shift(models.TextChoices):
        MORNING = "MORNING", "Morning"
        EVENING = "EVENING", "Evening"
        NIGHT = "NIGHT", "Night"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, blank=True, null=True
    )
    phone = models.CharField(max_length=15, blank=True)
    shift = models.CharField(max_length=20, choices=Shift.choices)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() if self.user else f"Nurse {self.id}"
