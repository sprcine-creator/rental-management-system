from django import forms
from .models import CommercialRate


class CommercialRateForm(forms.ModelForm):

    class Meta:
        model = CommercialRate

        fields = [
            "equipment",
            "negotiated_rate",
            "remarks",
        ]