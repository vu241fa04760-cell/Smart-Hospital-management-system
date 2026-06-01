from django import forms

from .models import Nurse


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ["user", "department", "phone", "shift", "is_active"]
