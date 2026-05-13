from django.shortcuts import render 
from django.http import HttpResponse
from .models import Patient

# Create your views here.

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})


def appointment_list(request):
    return HttpResponse("Appointment page")

def appointment_success(request):
    return HttpResponse("Appointment successful")

def doctors_list(request):
    return HttpResponse("Doctors list")