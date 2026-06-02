from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .forms import PrescriptionForm

# Create your views here.
def Prescription_list(request):
    prescriptions = Prescription.objects.filter(is_active=True).select_related('patient', 'doctor', 'medication')
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})

def add_Prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/add_Prescription.html', {'form': form})

def Prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'prescriptions/prescription_detail.html', {'prescription': prescription})

def deactivate_Prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    prescription.is_active = False
    prescription.save()
    return redirect('Prescription_list')