# Generated by Django 4.1.6 on 2023-08-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
