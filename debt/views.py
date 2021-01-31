from rest_framework import permissions, generics
from debt.serializers import DebtSerializer, PaymentSerializer, DebtReadSerializer, PaymentReadSerializer
from debt.models import Debt, Payment


class DebtList(generics.ListCreateAPIView):
    """
    List or create a Debt.
    """
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading a Debt
        to show the nested Payment in full.
        """
        if self.request.method in ('GET',):
            return DebtReadSerializer
        return DebtSerializer


class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Debt.
    """
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading a Debt
        to show the nested Payment in full.
        """
        if self.request.method in ('GET',):
            return DebtReadSerializer
        return DebtSerializer


class PaymentList(generics.ListCreateAPIView):
    """
    List or create a Payment.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading a Payment
        to show the nested Debt in full.
        """
        if self.request.method in ('GET',):
            return PaymentReadSerializer
        return PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Payment.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading a Payment
        to show the nested Debt in full.
        """
        if self.request.method in ('GET',):
            return PaymentReadSerializer
        return PaymentSerializer
