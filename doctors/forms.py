from django import forms

from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "user",
            "department",
            "specialization",
            "qualification",
            "phone",
            "consultation_fee",
            "available_days",
            "is_available",
        ]
