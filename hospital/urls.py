from django.contrib import admin
from django.urls import path, include
from patients import views as patient_views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', patient_views.patient_list),
    path('doctors/', include('doctors.urls')),
    path('staff/', include('staff.urls')),
    path('appointments/', include('appointments.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('inventory/', include('inventory.urls')),
    path('login/',  auth_views.LoginView.as_view(template_name='auth/login.html'),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('dashboard/',         patient_views.dashboard,          name='dashboard'),
    path('dashboard/doctor/',  patient_views.doctor_dashboard,   name='doctor_dashboard'),
    path('dashboard/patient/', patient_views.patient_dashboard,  name='patient_dashboard'),
    path('dashboard/admin/',   patient_views.admin_dashboard,    name='admin_dashboard'),
    path('notifications/', include('notifications.urls')),
    path('api/', include('api.urls')),
    path('', patient_views.home, name='home'),
    path('api/token/',         TokenObtainPairView.as_view(),  name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),
    path('api/schema/',  SpectacularAPIView.as_view(),                          name='schema'),
    path('api/docs/',    SpectacularSwaggerView.as_view(url_name='schema'),     name='swagger-ui'),
    path('api/redoc/',   SpectacularRedocView.as_view(url_name='schema'),       name='redoc'),

]