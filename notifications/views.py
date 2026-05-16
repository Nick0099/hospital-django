from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .utils import create_med_reminder, create_refill_alerts
from .models import Notification
from patients.models import Patient


@login_required
def notification_list(request):                          # ← was named 'notifications'
    try:
        patient = Patient.objects.get(phone=request.user.username)
        create_med_reminder(patient)                    # ← was create_med_reminder (missing s)
        create_refill_alerts(patient)
        notifications = Notification.objects.filter(patient=patient)
    except Patient.DoesNotExist:
        notifications = []
    return render(request, 'notifications/notification_list.html',
                  {'notifications': notifications})


@login_required
def mark_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.is_read = True
    notification.save()
    return redirect('notification_list')                 # ← was 'notifications_list'


@login_required
def mark_all_read(request):
    try:
        patient = Patient.objects.get(phone=request.user.username)
        Notification.objects.filter(patient=patient, is_read=False).update(is_read=True)
    except Patient.DoesNotExist:
        pass
    return redirect('notification_list')                 # ← was 'notifications_list'