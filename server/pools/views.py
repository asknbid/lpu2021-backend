from pools.models import Pool
from rest_framework import viewsets
from pools.serializers import PoolSerializer


class PoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
