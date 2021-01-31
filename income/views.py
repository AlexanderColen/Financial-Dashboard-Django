"""
API endpoints for Income & IncomeType CRUD.
"""
from rest_framework import permissions, generics
from income.serializers import IncomeSerializer, IncomeTypeSerializer, IncomeReadSerializer
from income.models import Income, IncomeType


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
        to show the nested IncomeType in full.
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
        to show the nested IncomeType in full.
        """
        if self.request.method in ('GET',):
            return IncomeReadSerializer
        return IncomeSerializer


class IncomeTypeList(generics.ListCreateAPIView):
    """
    List or create a IncomeType.
    """
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class IncomeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, create, update or delete a IncomeType.
    """
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
