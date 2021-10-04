from entries.models import Entry
from rest_framework import viewsets
from entries.serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

