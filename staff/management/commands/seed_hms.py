from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta

from staff.models import Department, Staff
from doctors.models import Doctor, Specialty, Qualification, Medication
from patients.models import Patient
from inventory.models import Supplier, InventoryItem
from appointments.models import Appointment
from prescriptions.models import Prescription

fake = Faker()


class Command(BaseCommand):
    help = "Full HMS database seeder"

    def handle(self, *args, **kwargs):

        # ---------------------------
        # LOAD EXISTING MASTER DATA
        # ---------------------------
        departments = list(Department.objects.all())
        specialties = list(Specialty.objects.all())
        qualifications = list(Qualification.objects.all())
        medications = list(Medication.objects.all())

        # ---------------------------
        # PATIENTS
        # ---------------------------
        patients = []
        for _ in range(100):
            patients.append(
                Patient(
                    name=fake.name(),
                    dob=fake.date_of_birth(minimum_age=1, maximum_age=90),
                    blood_type=random.choice(["A+","A-","B+","B-","O+","O-","AB+"]),
                    p_phone="98" + ''.join(str(random.randint(0,9)) for _ in range(8)),
                    e_phone="97" + ''.join(str(random.randint(0,9)) for _ in range(8)),
                    address=fake.address()[:100]
                )
            )

        Patient.objects.bulk_create(patients)
        patients = list(Patient.objects.all())

        self.stdout.write(self.style.SUCCESS("Patients added"))
        # ---------------------------
        # MASTER DATA (IMPORTANT)
        # ---------------------------

        if Specialty.objects.count() == 0:
            for name in ["Cardiology", "Neurology", "Pediatrics", "Orthopedics", "Radiology"]:
                Specialty.objects.create(name=name)

        if Qualification.objects.count() == 0:
            for name in ["MBBS", "MD", "MS", "FCPS"]:
                Qualification.objects.create(name=name)

        if Medication.objects.count() == 0:
            meds = [
                ("Paracetamol", "Painkiller"),
                ("Ibuprofen", "Painkiller"),
                ("Amoxicillin", "Antibiotic"),
                ("Cetirizine", "Antihistamine"),
            ]
            for name, cat in meds:
                Medication.objects.create(name=name, category=cat)

        # ---------------------------
        # DOCTORS
        # ---------------------------
        doctors = []
        for _ in range(15):
            doc = Doctor.objects.create(
                name="Dr. " + fake.name(),
                phone_number="98" + ''.join(str(random.randint(0,9)) for _ in range(8)),
                email=fake.unique.email(),
                license_number=str(random.randint(10000,99999)),
                shift=random.choice(["Morning","Afternoon","Night"]),
                specialties = list(Specialty.objects.all()),
                specialties = specialties or [Specialty.objects.first()]
            )

            doc.qualifications.set(random.sample(qualifications, 2))
            doc.can_prescribe.set(random.sample(medications, 2))

            doctors.append(doc)

        self.stdout.write(self.style.SUCCESS("Doctors added"))

        # ---------------------------
        # STAFF
        # ---------------------------
        roles = ["nurse","receptionist","lab_tech","pharmacist","cleaner","security","accountant"]

        for _ in range(30):
            Staff.objects.create(
                name=fake.name(),
                phone="98" + ''.join(str(random.randint(0,9)) for _ in range(8)),
                email=fake.unique.email(),
                role=random.choice(roles),
                shift=random.choice(["Morning","Afternoon","Night"]),
                salary=random.randint(20000,90000),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS("Staff added"))

        # ---------------------------
        # SUPPLIERS
        # ---------------------------
        suppliers = []
        for _ in range(8):
            suppliers.append(
                Supplier.objects.create(
                    name=fake.company(),
                    phone="98" + ''.join(str(random.randint(0,9)) for _ in range(8)),
                    email=fake.company_email(),
                    address=fake.address()
                )
            )

        self.stdout.write(self.style.SUCCESS("Suppliers added"))

        # ---------------------------
        # INVENTORY
        # ---------------------------
        items = [
            "Paracetamol", "Ibuprofen", "Amoxicillin",
            "Bandage", "Syringe", "Gloves",
            "Face Mask", "IV Set", "Cotton", "Thermometer"
        ]

        for item in items:
            InventoryItem.objects.create(
                name=item,
                category=random.choice(["medicine","equipment","consumable"]),
                unit=random.choice(["tablet","box","piece","bottle"]),
                quantity=random.randint(20,500),
                reorder_level=20,
                expiry_date=fake.date_between(start_date="+30d", end_date="+1000d"),
                price_per_unit=random.randint(10,500),
                supplier=random.choice(suppliers)
            )

        self.stdout.write(self.style.SUCCESS("Inventory added"))

        # ---------------------------
        # APPOINTMENTS
        # ---------------------------
        appointments = []

        for _ in range(200):
            appointments.append(
                Appointment(
                    patients=random.choice(patients),
                    doctor=random.choice(doctors),
                    date=fake.date_between(start_date="-60d", end_date="+30d"),
                    time=fake.time(),
                    status=random.choice(["scheduled","completed","cancelled","no_show"]),
                    reason=fake.sentence()
                )
            )

        Appointment.objects.bulk_create(appointments)
        appointments = list(Appointment.objects.all())

        self.stdout.write(self.style.SUCCESS("Appointments added"))

        # ---------------------------
        # PRESCRIPTIONS
        # ---------------------------
        completed = Appointment.objects.filter(status="completed")

        for appt in completed[:100]:
            Prescription.objects.create(
                patient=appt.patients,
                doctor=appt.doctor,
                appointment=appt,
                medication=random.choice(medications),
                dosage="500mg",
                frequency=random.choice(["Once","Twice","Thrice"]),
                start_date=appt.date,
                end_date=appt.date + timedelta(days=7),
                instructions="Take after meals"
            )

        self.stdout.write(self.style.SUCCESS("Prescriptions added"))

        self.stdout.write(self.style.SUCCESS("🎉 FULL HMS DATA SEED COMPLETE"))