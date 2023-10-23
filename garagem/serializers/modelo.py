from rest_framework.serializers import ModelSerializer

from models.modelo import Modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
