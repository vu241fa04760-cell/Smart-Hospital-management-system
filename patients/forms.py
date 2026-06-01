from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "user",
            "patient_id",
            "full_name",
            "age",
            "gender",
            "blood_group",
            "phone",
            "address",
            "medical_history",
        ]
