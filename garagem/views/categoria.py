from rest_framework.viewsets import ModelViewSet

from models.categoria import Categoria
from serializers.categoria import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
