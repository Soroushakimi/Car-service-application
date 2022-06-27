
from django.shortcuts import render
from core.models import Car

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from core.permissions import IsReception
from core.models import CarPart

from .serializers import CarSerializer, CarPartSerializer


class CarListApiView(APIView):

    permission_classes = [IsReception]
    def get(self, request):
        qs = Car.objects.all()
        serializer = CarSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)


class CarApiView(APIView):
    permission_classes = [IsReception]
    
    def get(self, request, pk):
        qs = Car.objects.get(id = pk)
        serializer = CarSerializer(qs, context={'request': request})
        return Response(serializer.data)


class CarPartListView(APIView):
    permission_classes = [IsReception]
    
    def get(self, request):
        qs = CarPart.objects.all()
        serializer = CarPartSerializer(qs, many=True, context={'request':request})
        return Response(serializer.data)

