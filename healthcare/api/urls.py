from django.urls import path
from .views import api_root
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView,
    DoctorListCreateView,
    DoctorRetrieveUpdateDestroyView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingRetrieveDestroyView,
    PatientDoctorsListView
)

urlpatterns = [
    # Authentication
     path('', api_root, name='api-root'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Patient management
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
    
    # Doctor management
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
    
    # Patient-Doctor mapping
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingRetrieveDestroyView.as_view(), name='mapping-detail'),
    path('mappings/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors-list'),
]