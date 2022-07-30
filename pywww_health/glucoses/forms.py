from django import forms

from .models import GlucoseMeasurement

class GlucoseForm(forms.ModelForm):
    class Meta:
        model = GlucoseMeasurement
        fields = "__all__"

    