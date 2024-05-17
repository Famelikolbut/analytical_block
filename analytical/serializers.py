from rest_framework import serializers

from .models import Analytical


class AnalyticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytical
        fields = ['id', 'name']
