
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path

from .views import CarListApiView, CarApiView, CarPartListView

urlpatterns = [
    path('car-list/', CarListApiView.as_view(), name='car_list'),
    path('get-car/<int:pk>', CarApiView.as_view(), name='get_car'),
    path('carpart-list/', CarPartListView.as_view(), name='carpart_list'),

]

