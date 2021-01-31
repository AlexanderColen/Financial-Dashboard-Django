"""
Define Debt & Payment models.
"""
from django.db import models

class Debt(models.Model):
    """
    Class for saving Debt information.
    """
    id = models.AutoField(primary_key=True)
    startDate = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    to = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    isLoan = models.BooleanField(default=True)
    isPaid = models.BooleanField(default=False)

    class Meta:
        ordering = ['startDate']

class Payment(models.Model):
    """
    Class for saving Payment information for a Debt.
    """
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='payments')

    class Meta:
        ordering = ['date']
