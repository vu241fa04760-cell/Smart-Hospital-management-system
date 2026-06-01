from django import forms

from .models import HospitalTiming


class HospitalTimingForm(forms.ModelForm):
    class Meta:
        model = HospitalTiming
        fields = ["department", "day_of_week", "opening_time", "closing_time", "is_closed"]
        widgets = {
            "opening_time": forms.TimeInput(attrs={"type": "time"}),
            "closing_time": forms.TimeInput(attrs={"type": "time"}),
        }
