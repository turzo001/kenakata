# Generated by Django 4.1.6 on 2024-01-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_predict'),
    ]

    operations = [
        migrations.AddField(
            model_name='predict',
            name='predicted_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
