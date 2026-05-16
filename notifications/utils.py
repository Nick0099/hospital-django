from .models import Notification
from django.utils import timezone
from datetime import timedelta
from prescriptions.models import Prescription
from appointments.models import Appointment

def create_med_reminder(patient):
    """Create medication reminder notifications for all active prescriptions of the patient."""
    prescriptions = Prescription.objects.filter(patient=patient, is_active=True)
    for prescription in prescriptions:
        already_exists = Notification.objects.filter(
            patient=patient,
            type='med_reminder',
            prescription=Prescription,
            created_at__date=timezone.now().date()
        ).exists()

    if not already_exists:
        Notification.objects.create(
            patient=patient,
            prescription=Prescription,
            type='med_reminder',
            message=f"Reminder: Take {Prescription.medicatrion} "
                    f"{Prescription.dosage} - {Prescription.get_frequency_display()}.",
        )
def create_refill_alerts(patient):
    """Alert patients when prescription is ending in 3 days."""
    prescriptions = Prescription.objects.filter(patient=patient, is_active=True)
    in_3_days = timezone.now() + timedelta(days=3)
    for prescription in prescriptions:
        if prescriptions.end_date <= in_3_days:
            already_exists = Notification.objects.filter(
                patient=patient,
                prescription=Prescription,
                type = 'refill',
            ).exists()
            if not already_exists:
                Notification.objects.create(
                    patient=patient,
                    prescription=Prescription,
                    type='refill',
                    message=f"Your prescription for {Prescription.medicatrion} "
                            f"is ending on {Prescription.end_date}. Please contact your doctor for a refill.",
                )

def create_appointment_reminders():
    """Remind patient 1 day before appointment."""
    tomorrow = timezone.now() + timedelta(days=1)
    if Appointment.date == tomorrow:
        already_exists = Notification.objects.filter(
            patient=Appointment.patient,
            appointment=Appointment,
            type='appointment',
        ).exists()
    if not already_exists:
        Notification.objects.create(
            patient=Appointment.patient,
            appointment=Appointment,
            type='appointment',
            message=f"Reminder: You have an appointment with Dr. {Appointment.doctor} "
                    f"on {Appointment.date.strftime('%Y-%m-%d %H:%M')}.",
        )