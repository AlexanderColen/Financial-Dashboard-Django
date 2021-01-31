"""
Serializers for encoding/decoding Debt & Payment models.
"""
from rest_framework import serializers
from debt.models import Debt, Payment


class DebtSerializer(serializers.ModelSerializer):
    """
    Serializer for Debt model.
    """
    class Meta:
        model = Debt
        fields = ['id', 'startDate', 'total', 'to', 'description', 'isLoan', 'isPaid']


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for Payment model.
    """
    class Meta:
        model = Payment
        fields = ['id', 'date', 'amount', 'debt']


class DebtReadSerializer(PaymentSerializer):
    """
    Serializer for reading of Debt model.
    """
    payments = PaymentSerializer(read_only=True, many=True)

    class Meta:
        model = Debt
        fields = ['id', 'startDate', 'total', 'to', 'description', 'isLoan', 'isPaid', 'payments']
        depth = 1


class PaymentReadSerializer(DebtSerializer):
    """
    Serializer for reading of Payment model.
    """
    debt = DebtSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'date', 'amount', 'debt']
        depth = 1
