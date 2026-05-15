from django.db import models
from patients.models import Patient
from doctors.models import Doctor,Medication
from appointments.models import Appointment

# Create your models here.

class prescription(models.Model):
    FREQUENCY_CHOICES = [
        ('Once', 'Once a day'),
        ('Twice', 'Twice a day'),
        ('Thrice', 'Three times a day'),
        ('Every_6hours', 'Every 6 hours'),
        ('Every_8_hours', 'Every 8 hours'),
        ('as_needed', 'As needed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()   
    instructions = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication} for {self.patient} prescribed by {self.doctor}"
    
    class Meta:
        ordering = ['-created_at']
        