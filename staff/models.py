from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
     SHIFT_CHOICES = [
        ('Morning', 'Morning (6am-2pm)'),
        ('Afternoon', 'Afternoon (2pm-10pm)'),
        ('Night', 'Night (10pm-6am)'),
    ]
     ROLE_CHOICES = [
         ('receptionist', 'Receptionist'),
         ('nurse','Nurse'),
         ('pharmacist','Pharmacist'),
         ('lab_tech', 'Lab Technician'),
         ('cleaner','Cleaner'),
         ('security','Security'),
         ('accountant','Accountant'),
         ('it', 'IT Staff'),
         ('other', 'Other'),
     ]
     name = models.CharField(max_length=100)
     phone = models.CharField(max_length=15)
     email = models.EmailField(unique=True)
     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
     shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
     salary = models.DecimalField(max_digits=10, decimal_places=2)
     joined_data = models.DateField(auto_now_add=True)
     is_active = models.BooleanField(default=True)
     department = models.ForeignKey(
         Department,
         on_delete=models.SET_NULL,
         null=True,
     )

def __str__(self):
    return f"{self.name} - {self.role}"