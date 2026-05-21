from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.api_overview,                  name='api-overview'),
    path('patients/',               views.PatientListCreate.as_view(),   name='patient-list-create'),
    path('patients/<int:pk>/',      views.PatientDetail.as_view(),       name='patient-detail'),
    path('doctors/',                views.DoctorListCreate.as_view(),    name='doctor-list-create'),
    path('doctors/<int:pk>/',       views.DoctorDetail.as_view(),        name='doctor-detail'),
    path('appointments/',           views.AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/',  views.AppointmentDetail.as_view(),   name='appointment-detail'),
    path('prescriptions/',          views.PrescriptionListCreate.as_view(), name='prescription-list-create'),
    path('prescriptions/<int:pk>/', views.PrescriptionDetail.as_view(), name='prescription-detail'),
    path('inventory/',              views.InventoryListCreate.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/',     views.InventoryDetail.as_view(),     name='inventory-detail'),
    path('inventory/low-stock/',    views.low_stock_alert,               name='low-stock-alert'),
]