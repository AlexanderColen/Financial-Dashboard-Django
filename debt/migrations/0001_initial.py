# Generated by Django 3.1.5 on 2021-01-31 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('to', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('isLoan', models.BooleanField(default=True)),
                ('isPaid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['startDate'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('debt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='debt.debt')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]