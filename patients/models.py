from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    blood_type = models.CharField(max_length=3)
    p_phone = models.CharField(max_length=15)
    e_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name    