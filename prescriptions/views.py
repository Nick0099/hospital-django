from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .forms import PrescriptionForm

# Create your views here.
def Prescription_list(request):
    Prescriptions = Prescription.objects.filter(is_active=True).select_related('patient', 'doctor', 'medication')
    return render(request, 'Prescriptions/Prescription_list.html', {'Prescriptions': Prescriptions})

def add_Prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'Prescriptions/add_Prescription.html', {'form': form})

def Prescription_detail(request, pk):
    Prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'Prescriptions/Prescription_detail.html', {'Prescription': Prescription})

def deactivate_Prescription(request, pk):
    Prescription = get_object_or_404(Prescription, pk=pk)
    Prescription.is_active = False
    Prescription.save()
    return redirect('Prescription_list')