from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patients', 'doctor', 'date', 'time', 'status']
    list_filter = ['status', 'date', 'doctor']
    search_fields = ['patients__name', 'doctor__name']