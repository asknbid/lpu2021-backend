from pools.models import Pool
from rest_framework import serializers


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ['id', 'name', 'max_entries']