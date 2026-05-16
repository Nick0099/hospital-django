from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient
from django.contrib.auth.decorators import login_required


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})


@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser:
        return redirect('admin_dashboard')
    elif user.groups.filter(name='Doctors').exists():
        return redirect('doctor_dashboard')
    elif user.groups.filter(name='Patients').exists():
        return redirect('patient_dashboard')
    elif user.groups.filter(name='Staff').exists():
        return redirect('staff_dashboard')
    else:
        return render(request, 'dashboard/no_role.html')


@login_required
def doctor_dashboard(request):
    from appointments.models import Appointment
    from doctors.models import Doctor
    try:
        doctor = Doctor.objects.get(email=request.user.email)
        appointments = Appointment.objects.filter(doctor=doctor).order_by('date')[:10]
    except Doctor.DoesNotExist:
        doctor = None
        appointments = []
    return render(request, 'dashboard/doctor.html', {   # ← was missing return render
        'doctor': doctor,
        'appointments': appointments,
    })


@login_required
def patient_dashboard(request):
    from appointments.models import Appointment
    from prescriptions.models import Prescription           # ← capital P
    try:
        patient = Patient.objects.get(p_phone=request.user.username)
        appointments  = Appointment.objects.filter(patient=patient).order_by('-date')[:10]
        prescriptions = Prescription.objects.filter(patient=patient, is_active=True)
    except Patient.DoesNotExist:
        patient = None
        appointments = []
        prescriptions = []
    return render(request, 'dashboard/patient.html', {
        'patient':       patient,
        'appointments':  appointments,
        'prescriptions': prescriptions,
    })


@login_required
def admin_dashboard(request):
    from appointments.models import Appointment
    from doctors.models import Doctor
    from inventory.models import InventoryItem
    if not request.user.is_superuser and not request.user.groups.filter(name='Staff').exists():
        return redirect('dashboard')
    total_patients     = Patient.objects.count()           # ← was Patient.object (missing s)
    total_doctors      = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    low_stock          = [i for i in InventoryItem.objects.all() if i.is_low_stock()]
    return render(request, 'dashboard/admin.html', {
        'total_patients':     total_patients,
        'total_doctors':      total_doctors,
        'total_appointments': total_appointments,
        'low_stock':          low_stock,
    })