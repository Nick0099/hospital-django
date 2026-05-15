from django.shortcuts import render, redirect, get_object_or_404
from .models import prescription
from .forms import PrescriptionForm

# Create your views here.
def prescription_list(request):
    prescriptions = prescription.objects.filter(is_active=True).select_related('patient', 'doctor', 'medication')
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})

def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/add_prescription.html', {'form': form})

def prescription_detail(request, pk):
    prescription = get_object_or_404(prescription, pk=pk)
    return render(request, 'prescriptions/prescription_detail.html', {'prescription': prescription})

def deactivate_prescription(request, pk):
    prescription = get_object_or_404(prescription, pk=pk)
    prescription.is_active = False
    prescription.save()
    return redirect('prescription_list')