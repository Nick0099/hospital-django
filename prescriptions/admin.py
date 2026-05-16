from django.contrib import admin
from .models import Prescription

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'medication', 'dosage', 'frequency', 'is_active']
    search_fields =['patient__name', 'doctor__name', 'medication__name']
    list_filter = ['is_active', 'frequency','doctor']
# Register your models here.
