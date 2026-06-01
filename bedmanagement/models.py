from django.db import models


class Bed(models.Model):
    class BedType(models.TextChoices):
        GENERAL = "GENERAL", "General"
        ICU = "ICU", "ICU"
        EMERGENCY = "EMERGENCY", "Emergency"
        PRIVATE = "PRIVATE", "Private"

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        OCCUPIED = "OCCUPIED", "Occupied"
        MAINTENANCE = "MAINTENANCE", "Maintenance"

    ward = models.CharField(max_length=80)
    bed_number = models.CharField(max_length=20, unique=True)
    bed_type = models.CharField(max_length=20, choices=BedType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    patient = models.ForeignKey(
        "patients.Patient", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.ward} - {self.bed_number}"
