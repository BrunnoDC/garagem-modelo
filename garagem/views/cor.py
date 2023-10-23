from rest_framework.viewsets import ModelViewSet

from models.cor import Cor
from serializers.cor import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
