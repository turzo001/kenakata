# Generated by Django 4.1.6 on 2023-09-01 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_orderplaced_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment_method',
        ),
    ]
