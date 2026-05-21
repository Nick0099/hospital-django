from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from prescriptions.models import Prescription
from inventory.models import InventoryItem

from .serializers import (
    PatientSerializer, DoctorSerializer, AppointmentSerializer,
    PrescriptionSerializer, InventoryItemSerializer
)


@api_view(['GET'])
def api_overview(request):
    return Response({
        'patients':      '/api/patients/',
        'doctors':       '/api/doctors/',
        'appointments':  '/api/appointments/',
        'prescriptions': '/api/prescriptions/',
        'inventory':     '/api/inventory/',
        'docs':          '/api/docs/',
        'token':         '/api/token/',
    })


class PatientListCreate(generics.ListCreateAPIView):
    queryset           = Patient.objects.all()
    serializer_class   = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [SearchFilter, OrderingFilter]
    search_fields      = ['name', 'blood_type', 'p_phone']
    ordering_fields    = ['name', 'dob']


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Patient.objects.all()
    serializer_class   = PatientSerializer
    permission_classes = [IsAuthenticated]


class DoctorListCreate(generics.ListCreateAPIView):
    queryset           = Doctor.objects.all()
    serializer_class   = DoctorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['specialty', 'shift', 'is_available']
    search_fields      = ['name', 'license_number']
    ordering_fields    = ['name']


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Doctor.objects.all()
    serializer_class   = DoctorSerializer
    permission_classes = [IsAuthenticated]


class AppointmentListCreate(generics.ListCreateAPIView):
    queryset           = Appointment.objects.all()
    serializer_class   = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['status', 'doctor']
    search_fields      = ['patients__name', 'doctor__name', 'reason']
    ordering_fields    = ['date', 'time']


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Appointment.objects.all()
    serializer_class   = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class PrescriptionListCreate(generics.ListCreateAPIView):
    queryset           = Prescription.objects.filter(is_active=True)
    serializer_class   = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [DjangoFilterBackend, SearchFilter]
    filterset_fields   = ['is_active', 'doctor', 'frequency']
    search_fields      = ['patient__name', 'medication__name']


class PrescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Prescription.objects.all()
    serializer_class   = PrescriptionSerializer
    permission_classes = [IsAuthenticated]


class InventoryListCreate(generics.ListCreateAPIView):
    queryset           = InventoryItem.objects.all()
    serializer_class   = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['category', 'unit']
    search_fields      = ['name']
    ordering_fields    = ['name', 'quantity', 'expiry_date']


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset           = InventoryItem.objects.all()
    serializer_class   = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def low_stock_alert(request):
    items      = [i for i in InventoryItem.objects.all() if i.is_low_stock()]
    serializer = InventoryItemSerializer(items, many=True)
    return Response(serializer.data)