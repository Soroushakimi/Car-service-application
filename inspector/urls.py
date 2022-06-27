from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CarInspectorView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('car-is-finished/<int:pk>', CarInspectorView.as_view(), name="car_is_finished"),
    
]
