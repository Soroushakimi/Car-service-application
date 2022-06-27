from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from django.contrib import admin
from django.urls import path

from .views import CarView

urlpatterns = [
    path('car-create/', CarView.as_view(), name='car_list'),
    path('car-update/<int:pk>', CarView.as_view(), name='car-update'),
    
]

