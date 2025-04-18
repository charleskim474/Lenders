# Generated by Django 5.1.7 on 2025-04-07 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
                ('NIN', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('subscription', models.BooleanField(default=False)),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Aggreements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField(auto_now_add=True)),
                ('aggreement', models.ImageField(upload_to='')),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.borrower')),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.lender')),
            ],
        ),
        migrations.AddField(
            model_name='borrower',
            name='lender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.lender'),
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_Date', models.DateField(auto_now_add=True)),
                ('loan_amount', models.IntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=3, max_digits=5)),
                ('processing_fee', models.IntegerField()),
                ('total_amm', models.DecimalField(decimal_places=3, max_digits=9)),
                ('duration', models.IntegerField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.borrower')),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.lender')),
            ],
        ),
        migrations.CreateModel(
            name='Collateral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('proof', models.ImageField(upload_to='')),
                ('asset_photo', models.ImageField(upload_to='')),
                ('aggr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.aggreements')),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.borrower')),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.lender')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.loans')),
            ],
        ),
        migrations.AddField(
            model_name='aggreements',
            name='loan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.loans'),
        ),
        migrations.CreateModel(
            name='Repayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('paid', models.IntegerField()),
                ('bal', models.DecimalField(decimal_places=3, max_digits=9)),
                ('percentage_paid', models.DecimalField(decimal_places=3, max_digits=5)),
                ('time_left', models.IntegerField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.borrower')),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.lender')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kimtech.loans')),
            ],
        ),
    ]
