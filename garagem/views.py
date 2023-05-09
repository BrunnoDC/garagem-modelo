from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Cor, Acessório, Modelo
from garagem.serializers import CategoriaSerializer, CorSerializer, AcessórioSerializer, ModeloSerializer



class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class AcessórioViewSet(ModelViewSet):
    queryset = Acessório.objects.all()
    serializer_class = AcessórioSerializer
class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
