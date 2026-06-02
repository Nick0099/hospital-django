from django.shortcuts import render, get_object_or_404
from .models import Staff
from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from inventory.models import InventoryItem

def staff_list(request):
    staff = Staff.objects.filter(is_active=True).select_related('department')
    return render(request, 'staff/staff_list.html', {'staff': staff})

def staff_detail(request, pk):
    member = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_detail.html', {'member': member})

def staff_dashboard(request):
    context = {
        "total_patients": Patient.objects.count(),
        "total_doctors": Doctor.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "low_stock": InventoryItem.objects.filter(quantity__lte=20),
    }
    return render(request, "staff/dashboard.html", context)