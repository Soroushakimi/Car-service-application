
from rest_framework import serializers

from core.models import CarPart, Car


class CarTechnicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('is_repaired',)


class CarPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ("name","part")
        read_only_fields = ('part',)

    def create(self, validated_data):
        name = validated_data.get("name")
        car = Car.objects.filter(name = name).first()
        partt = CarPart.objects.get(id=self.context["part_id"])
        car.part.add(partt)
        car.save()
        return car

    

