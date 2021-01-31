from django.db import models

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    source = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.ForeignKey('Type', on_delete=models.SET_DEFAULT, default='-')

    class Meta:
        ordering = ['date']

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=25, blank=False)

    class Meta:
        ordering = ['name']
