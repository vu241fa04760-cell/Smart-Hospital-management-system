from django.db import models


class HospitalTiming(models.Model):
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, blank=True, null=True
    )
    day_of_week = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        department = self.department.name if self.department else "Hospital"
        return f"{department} - {self.day_of_week}"
