from django import forms
from .models import prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = prescription
        fields = ['patient', 'doctor', 'medication', 'dosage', 'frequency', 'appointment', 'start_date', 'end_date', 'is_active','end_date','instructions']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
