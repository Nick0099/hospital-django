from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor, Specialty
from datetime import date, time


class AppointmentModelTest(TestCase):

    def setUp(self):
        self.specialty = Specialty.objects.create(name='General')
        self.patient = Patient.objects.create(
            name       = 'Test Patient',
            dob        = date(1990, 1, 1),
            blood_type = 'O+',
            p_phone    = '9840000000',
            e_phone    = '9840000001',
            address    = 'KTM',
        )
        self.doctor = Doctor.objects.create(
            name           = 'Test Doctor',
            phone_number   = '9840000002',      # ← phone_number
            email          = 'doc@test.com',
            license_number = 'NMC-99999',
            shift          = 'Morning',          # ← capital M
            specialty      = self.specialty,
        )
        self.appointment = Appointment.objects.create(
            patients = self.patient,
            doctor  = self.doctor,
            date    = date(2026, 6, 1),
            time    = time(10, 0),
            status  = 'scheduled',
            reason  = 'Regular checkup',
        )

    def test_appointment_created(self):
        self.assertEqual(self.appointment.status, 'scheduled')
        self.assertEqual(self.appointment.reason, 'Regular checkup')

    def test_appointment_links_patient_and_doctor(self):
        self.assertEqual(self.appointment.patients.name, 'Test Patient')
        self.assertEqual(self.appointment.doctor.name, 'Test Doctor')

    def test_appointment_str(self):
        result = str(self.appointment)
        self.assertIn('Test Patient', result)

    def test_appointment_can_be_cancelled(self):
        self.appointment.status = 'cancelled'
        self.appointment.save()
        updated = Appointment.objects.get(pk=self.appointment.pk)
        self.assertEqual(updated.status, 'cancelled')


class AppointmentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_appointment_list_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/appointments/')
        self.assertEqual(response.status_code, 200)

    def test_book_appointment_page_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/appointments/book/')
        self.assertEqual(response.status_code, 200)