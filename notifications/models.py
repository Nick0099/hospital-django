from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from prescriptions.models import Prescription

class Notification(models.Model):
    TYPE_CHOICES = [
        ('med_reminder', 'Medication Reminder'),
        ('refill', 'Refill Alert'),
        ('appointment', 'Appointment Reminder'),
        ('general', 'General'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)

# Create your models here.

prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
    return f"{self.get_type_display()} for {self.patient} "

class Meta:
    ordering = ['-created_at']
    