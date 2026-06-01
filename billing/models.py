from django.db import models


class Bill(models.Model):
    class Status(models.TextChoices):
        UNPAID = "UNPAID", "Unpaid"
        PARTIAL = "PARTIAL", "Partial"
        PAID = "PAID", "Paid"

    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    appointment = models.ForeignKey(
        "appointment.Appointment", on_delete=models.SET_NULL, blank=True, null=True
    )
    bill_number = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UNPAID)
    issued_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill_number} - {self.patient}"
