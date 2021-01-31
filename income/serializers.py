"""
Serializers for encoding/decoding Income & IncomeType models.
"""
from rest_framework import serializers
from income.models import Income, IncomeType


class IncomeSerializer(serializers.ModelSerializer):
    """
    Serializer for Income model.
    """
    class Meta:
        model = Income
        fields = ['id', 'date', 'amount', 'source', 'description', 'type']


class IncomeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for IncomeType model.
    """
    class Meta:
        model = IncomeType
        fields = ['id', 'name']


class IncomeReadSerializer(IncomeSerializer):
    """
    Serializer for reading of Income model.
    """
    type = IncomeTypeSerializer(read_only=True)
