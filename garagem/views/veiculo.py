from rest_framework.viewsets import ModelViewSet

from models.veiculo import Veiculo
from serializers.veiculo import (
    VeiculoSerializer,
    VeiculoDetailSerializer,
    VeiculoListSerializer,
)


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer

    serializer_class = VeiculoSerializer
