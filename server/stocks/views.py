from stocks.models import Stock
from rest_framework import viewsets
from stocks.serializers import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
