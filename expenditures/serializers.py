from rest_framework import serializers
from expenditures.models import Expenditure, Type


class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id', 'date', 'amount', 'vendor', 'description', 'type']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class ExpenditureReadSerializer(ExpenditureSerializer):
    type = TypeSerializer(read_only=True)
