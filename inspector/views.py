from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import Car
from core.permissions import IsInspector

from .serializer import CarInspectorSerializer


class CarInspectorView(APIView):
    permission_classes = [IsInspector]
    
    def patch(self, request, pk):
        qs = Car.objects.get(id=pk)
        serializer = CarInspectorSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "True/False shod"}, status=status.HTTP_202_ACCEPTED)

