from rest_framework.viewsets import ModelViewSet

from models.marca import Marca
from serializers.marca import MarcaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
