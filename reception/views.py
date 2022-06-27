from django.shortcuts import render
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status

from core.models import Car

from .serializers import CarReseptionSerializer
from core.permissions import IsReception


class CarView(APIView):
    permission_classes = [IsReception]
    
    def post(self, request):
        serializer = CarReseptionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"status": "success", "message": "ijad shod"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)
    
    def patch(self, request, pk):
        qs = Car.objects.get(id=pk)
        serializer = CarReseptionSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "update shod"}, status=status.HTTP_200_OK)



