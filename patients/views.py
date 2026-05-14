from django.shortcuts import render 
from django.http import HttpResponse
from .models import Patient

# Create your views here.

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})
