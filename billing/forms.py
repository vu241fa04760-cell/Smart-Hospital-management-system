from django import forms

from .models import Bill


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            "patient",
            "appointment",
            "bill_number",
            "description",
            "total_amount",
            "paid_amount",
            "status",
        ]
