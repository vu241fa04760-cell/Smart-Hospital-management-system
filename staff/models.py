from django.conf import settings
from django.db import models


class Staff(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, blank=True, null=True
    )
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    joining_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        name = self.user.get_full_name() if self.user else "Staff"
        return f"{name} - {self.designation}"
