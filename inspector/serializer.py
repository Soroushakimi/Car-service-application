from rest_framework import serializers

from core.models import Car


class CarInspectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('is_finished',)

