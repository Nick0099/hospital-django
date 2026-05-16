from django.urls import path
from . import views
urlpatterns = [
    path('', views.Prescription_list, name='Prescription_list'),
    path('add/', views.add_Prescription, name='add_prescription'),
    path('<int:pk>/', views.Prescription_detail, name='prescription_detail'),
    path('<int:pk>/deactivate/', views.deactivate_Prescription, name='deactivate_prescription')
]