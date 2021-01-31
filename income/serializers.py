from django.contrib.auth.models import User, Group
from rest_framework import serializers
from income.models import Income, Type


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'date', 'amount', 'source', 'description', 'type']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class IncomeReadSerializer(IncomeSerializer):
    type = TypeSerializer(read_only=True)
