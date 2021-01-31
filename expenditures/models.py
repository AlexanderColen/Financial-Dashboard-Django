"""
Define Expenditure & ExpenditureType models.
"""
from django.db import models

class Expenditure(models.Model):
    """
    Class for saving Expenditure information.
    """
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    vendor = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.ForeignKey('ExpenditureType', on_delete=models.SET_DEFAULT, default='-')

    class Meta:
        ordering = ['date']

class ExpenditureType(models.Model):
    """
    Class for saving ExpenditureType information for Expenditures.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=25, blank=False)

    class Meta:
        ordering = ['name']
