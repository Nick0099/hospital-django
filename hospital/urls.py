from django.contrib import admin
from django.urls import path, include
from patients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', views.patient_list),
    path('doctors/', include('doctors.urls')),
    path('staff/', include('staff.urls')),
    path('appointments/', include('appointments.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('inventory/', include('inventory.urls')),
    
]