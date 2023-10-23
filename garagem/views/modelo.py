from rest_framework.viewsets import ModelViewSet

from models.modelo import Modelo
from serializers.modelo import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
