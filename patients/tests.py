from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Patient
from datetime import date


class PatientModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            name       = 'Ram Shrestha',
            dob        = date(1990, 1, 15),
            blood_type = 'A+',
            p_phone    = '9841000000',
            e_phone    = '9841000001',
            address    = 'Kathmandu',
        )

    def test_patient_created_successfully(self):
        self.assertEqual(self.patient.name, 'Ram Shrestha')
        self.assertEqual(self.patient.blood_type, 'A+')
        self.assertEqual(self.patient.p_phone, '9841000000')

    def test_patient_str(self):
        self.assertEqual(str(self.patient), 'Ram Shrestha')

    def test_patient_count(self):
        self.assertEqual(Patient.objects.count(), 1)

    def test_patient_dob(self):
        self.assertEqual(self.patient.dob, date(1990, 1, 15))


class PatientListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.patient = Patient.objects.create(
            name       = 'Sita Sharma',
            dob        = date(1995, 5, 20),
            blood_type = 'B+',
            p_phone    = '9841111111',
            e_phone    = '9841111112',
            address    = 'Lalitpur',
        )

    def test_patient_list_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, 200)

    def test_patient_list_shows_patient_name(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/patients/')
        self.assertContains(response, 'Sita Sharma')

    def test_patient_list_uses_correct_template(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/patients/')
        self.assertTemplateUsed(response, 'patients/patient_list.html')