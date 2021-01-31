from rest_framework import serializers
from debt.models import Debt, Payment


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'startDate', 'total', 'to', 'description', 'isLoan', 'isPaid']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'date', 'amount', 'debt']


class PaymentReadSerializer(DebtSerializer):
    debt = DebtSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'date', 'amount', 'debt']
        depth = 1

class DebtReadSerializer(PaymentSerializer):
    payments = PaymentSerializer(read_only=True, many=True)

    class Meta:
        model = Debt
        fields = ['id', 'startDate', 'total', 'to', 'description', 'isLoan', 'isPaid', 'payments']
        depth = 1