from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Cor, Acessório, Modelo

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class AcessórioSerializer(ModelSerializer):
    class Meta:
        model = Acessório
        fields = "__all__"

class ModeloSerializer(ModelSerializer):
    class meta:
        model = Modelo
        fields = "__all__"