from rest_framework import serializers
from .models import PlanEntrenamiento

class PlanEntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntrenamiento
        fields = '__all__'