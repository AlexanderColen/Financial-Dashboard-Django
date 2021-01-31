from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from income.serializers import IncomeSerializer, TypeSerializer, IncomeReadSerializer
from income.models import Income, Type


class IncomeList(generics.ListCreateAPIView):
    """
    List or create an Income.
    """
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading an Income
        to show the nested Type in full.
        """
        if self.request.method in ('GET',):
            return IncomeReadSerializer
        return IncomeSerializer


class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, create, update or delete an Income.
    """
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading an Income
        to show the nested Type in full.
        """
        if self.request.method in ('GET',):
            return IncomeReadSerializer
        return IncomeSerializer


class TypeList(generics.ListCreateAPIView):
    """
    List or create a Type.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, create, update or delete a Type.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]