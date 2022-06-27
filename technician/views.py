
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Car, CarPart
from core.permissions import IsTechnician
from .serializer import CarPartSerializer, CarTechnicianSerializer


class CarRepairedView(APIView):
    permission_classes = [IsTechnician]

    def patch(self, request, pk):
        qs = Car.objects.get(id=pk)
        serializer = CarTechnicianSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "True/False shod"}, status=status.HTTP_200_OK)


class CarPartView(APIView):
    permission_classes = [IsTechnician]
    
    def post(self, request):
        serializer = CarPartSerializer(data=request.data, context={"part_id": request.query_params.get("part_id")})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "ezafe shod"}, status=status.HTTP_200_OK)


class CarPartDeleteView(APIView):
    permission_classes = [IsTechnician]

    def delete(self, request):
        serializer = CarPartSerializer(data=request.data, context={"part_id": request.query_params.get("part_id")})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "ezafe shod"}, status=status.HTTP_200_OK)

