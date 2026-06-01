from django import forms

from .models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["user", "department", "designation", "phone", "joining_date", "is_active"]
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),
        }
