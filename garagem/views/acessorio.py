from rest_framework.viewsets import ModelViewSet

from models.acessorio import Acessorio
from serializers.acessorio import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
