"""
Serializers for encoding/decoding Expenditures & Type models.
"""
from rest_framework import serializers
from expenditures.models import Expenditure, ExpenditureType


class ExpenditureSerializer(serializers.ModelSerializer):
    """
    Serializer for Expenditure model.
    """
    class Meta:
        model = Expenditure
        fields = ['id', 'date', 'amount', 'vendor', 'description', 'type']


class ExpenditureTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for ExpenditureType model.
    """
    class Meta:
        model = ExpenditureType
        fields = ['id', 'name']


class ExpenditureReadSerializer(ExpenditureSerializer):
    """
    Serializer for reading of Expenditure model.
    """
    type = ExpenditureTypeSerializer(read_only=True)
