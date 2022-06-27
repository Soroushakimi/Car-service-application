
from rest_framework import serializers

from core.models import Car



class CarReseptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('name','id')


