from rest_framework import serializers
from patients.models import Patient
from doctors.models import Doctor, Specialty
from appointments.models import Appointment
from prescriptions.models import Prescription
from inventory.models import InventoryItem
from notifications.models import Notification

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name','phone_number', 'specialty','shift','is_available','license_number']

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id','patient_name', 'doctor','doctor_name','date','time', 'status', 'reason','notes']
    
class PrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    medication_name = serializers.CharField(source='medication.name', read_only=True)

    class Meta:
        model = Prescription
        fields = ['id', 'patient','patient_name', 'doctor','doctor_name','medication','medication_name','dosage','frequency','start_date','end_date','is_active']

class InventoryItemSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.SerializerMethodField()

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'category', 'quantity', 'unit','reorder_level','expeiry_date','price_per_unit','is_low_stock']

def get_is_low_stock(self, obj):
    return obj.is_low_stock()


