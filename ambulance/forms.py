from django import forms

from .models import Ambulance


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ["vehicle_number", "driver_name", "driver_phone", "current_location", "status"]
