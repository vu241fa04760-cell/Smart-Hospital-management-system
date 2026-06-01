from django.db import models


class Prescription(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.SET_NULL, null=True)
    medicines = models.TextField(help_text="Medicine name, dosage, and duration")
    notes = models.TextField(blank=True)
    prescribed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient}"
