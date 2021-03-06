# Generated by Django 3.2.8 on 2021-10-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='exp_return',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='exp_risk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='ticker_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
