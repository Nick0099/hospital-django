from django.contrib import admin
from django.urls import path
from patients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/book/', views.appointment_list, name='book_appointment'),
    path('appointments/success/', views.appointment_success, name='appointment_success'),
    path('doctors/', views.doctors_list, name='doctors_list'),
]
