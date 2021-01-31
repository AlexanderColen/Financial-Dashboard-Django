from rest_framework import permissions, generics
from expenditures.serializers import ExpenditureSerializer, TypeSerializer, ExpenditureReadSerializer
from expenditures.models import Expenditure, Type


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
        to show the nested Type in full.
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
        to show the nested Type in full.
        """
        if self.request.method in ('GET',):
            return ExpenditureReadSerializer
        return ExpenditureSerializer


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