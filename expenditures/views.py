"""
API endpoints for Expenditure & ExpenditureType CRUD.
"""
from rest_framework import permissions, generics
from expenditures.serializers import ExpenditureSerializer, ExpenditureTypeSerializer, ExpenditureReadSerializer
from expenditures.models import Expenditure, ExpenditureType


class ExpenditureList(generics.ListCreateAPIView):
    """
    List or create an Expenditure.
    """
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading an Expenditure
        to show the nested ExpenditureType in full.
        """
        if self.request.method in ('GET',):
            return ExpenditureReadSerializer
        return ExpenditureSerializer


class ExpenditureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, create, update or delete an Expenditure.
    """
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """"
        Override the serializer class when reading an Expenditure
        to show the nested ExpenditureType in full.
        """
        if self.request.method in ('GET',):
            return ExpenditureReadSerializer
        return ExpenditureSerializer


class ExpenditureTypeList(generics.ListCreateAPIView):
    """
    List or create a ExpenditureType.
    """
    queryset = ExpenditureType.objects.all()
    serializer_class = ExpenditureTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenditureTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, create, update or delete a ExpenditureType.
    """
    queryset = ExpenditureType.objects.all()
    serializer_class = ExpenditureTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
