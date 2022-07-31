from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from dal import autocomplete

from .models import BloodPressureMeasurement


class BloodPressureMeasurementForm(forms.ModelForm):
    class Meta:
        model = BloodPressureMeasurement
        fields = ['systolic_blood_pressure',
                  'diastolic_blood_pressure',
                  'pulse',
                  'measurement_datetime']
        labels = {
            'systolic_blood_pressure': 'Ciśnienie skurczowe:',
            'diastolic_blood_pressure': 'Ciśnienie rozkurczowe:',
            'pulse': 'Puls:',
            'measurement_datetime': 'Data pomiaru:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj pomiar',
                'systolic_blood_pressure',
                'diastolic_blood_pressure',
                'pulse',
                'measurement_datetime'
            ),
            ButtonHolder(
                Submit('submit', 'zapisz', css_class='btn btn-outline-light me-2'),
                css_class='text-end',
            )
        )
