from django.shortcuts import render, get_object_or_404
from .models import Staff

def staff_list(request):
    staff = Staff.objects.filter(is_active=True).select_related('department')
    return render(request, 'staff/staff_list.html', {'staff': staff})

def staff_detail(request, pk):
    member = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_detail.html', {'member': member})