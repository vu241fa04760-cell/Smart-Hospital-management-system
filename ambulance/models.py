from django.db import models


class Ambulance(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        DISPATCHED = "DISPATCHED", "Dispatched"
        MAINTENANCE = "MAINTENANCE", "Maintenance"

    vehicle_number = models.CharField(max_length=30, unique=True)
    driver_name = models.CharField(max_length=120)
    driver_phone = models.CharField(max_length=15)
    current_location = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)

    def __str__(self):
        return f"{self.vehicle_number} - {self.driver_name}"
