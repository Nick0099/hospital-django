from django.db import models

# Create your models here.
class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning (6am-2pm)'),
        ('Afternoon', 'Afternoon (2pm-10pm)'),
        ('Night', 'Night (10pm-6am)'),
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    is_available = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.SET_NULL,
        null=True
    )
    qualifications = models.ManyToManyField(Qualification)
    can_prescribe = models.ManyToManyField(Medication)

    def __str__(self):
        return f"{self.name} - {self.specialty}"
