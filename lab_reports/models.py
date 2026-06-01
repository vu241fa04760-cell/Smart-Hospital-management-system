from django.db import models


class LabReport(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        READY = "READY", "Ready"
        DELIVERED = "DELIVERED", "Delivered"

    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        "doctors.Doctor", on_delete=models.SET_NULL, blank=True, null=True
    )
    test_name = models.CharField(max_length=120)
    result = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    report_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_name} - {self.patient}"
