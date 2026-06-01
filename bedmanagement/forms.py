from django import forms

from .models import Bed


class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ["ward", "bed_number", "bed_type", "status", "patient"]
