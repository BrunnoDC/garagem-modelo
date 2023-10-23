from rest_framework.serializers import ModelSerializer

from models.acessorio import Acessorio


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
