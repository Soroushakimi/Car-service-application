
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path

from .views import CarRepairedView, CarPartView


urlpatterns = [
    path('car-is-repaired/<int:pk>', CarRepairedView.as_view(), name='car_is_repaired'),
    path('car-part/', CarPartView.as_view(), name='car_part'),

]

