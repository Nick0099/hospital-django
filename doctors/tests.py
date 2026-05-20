from django.test import TestCase
from .models import Doctor, Specialty, Qualification, Medication
from datetime import date


class SpecialtyModelTest(TestCase):

    def setUp(self):
        self.specialty = Specialty.objects.create(name='Cardiology')

    def test_specialty_created(self):
        self.assertEqual(self.specialty.name, 'Cardiology')

    def test_specialty_str(self):
        self.assertEqual(str(self.specialty), 'Cardiology')


class DoctorModelTest(TestCase):

    def setUp(self):
        self.specialty = Specialty.objects.create(name='Neurology')
        self.doctor = Doctor.objects.create(
            name           = 'Dr. Hari Bahadur',
            phone_number   = '9841222222',      # ← phone_number not phone
            email          = 'hari@hospital.com',
            license_number = 'NMC-12345',
            shift          = 'Morning',          # ← capital M matches your choices
            specialty      = self.specialty,
        )

    def test_doctor_created(self):
        self.assertEqual(self.doctor.name, 'Dr. Hari Bahadur')
        self.assertEqual(self.doctor.shift, 'Morning')

    def test_doctor_str(self):
        self.assertIn('Dr. Hari Bahadur', str(self.doctor))

    def test_doctor_is_available_by_default(self):
        self.assertTrue(self.doctor.is_available)

    def test_doctor_specialty_linked(self):
        self.assertEqual(self.doctor.specialty.name, 'Neurology')

    def test_doctor_can_be_marked_unavailable(self):
        self.doctor.is_available = False
        self.doctor.save()
        updated = Doctor.objects.get(pk=self.doctor.pk)
        self.assertFalse(updated.is_available)