from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'supplier', 'reorder_level','expiry_date','category','unit','price_per_unit']
        widjets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
        