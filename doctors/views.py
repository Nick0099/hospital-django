from django.shortcuts import render, get_object_or_404
from .models import Doctor

# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.filter(is_available=True).select_related('specialty')
    return render(request, 'doctors/doctors_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})