# Generated by Django 4.1.6 on 2024-01-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_orderplaced_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='predicted_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
