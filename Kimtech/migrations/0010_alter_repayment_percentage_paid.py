# Generated by Django 5.1.7 on 2025-04-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kimtech', '0009_loans_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repayment',
            name='percentage_paid',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
