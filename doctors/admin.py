from django.contrib import admin
from .models import Doctor, Specialty, Qualification, Medication
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'shift', 'is_available')
    list_filter = ('specialty', 'shift', 'is_available')
    search_fields = ('name', 'email', 'license_number')
    filter_horizontal = ('qualifications', 'can_prescribe')

admin.site.register(Specialty)
admin.site.register(Qualification)
admin.site.register(Medication)
