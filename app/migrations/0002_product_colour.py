# Generated by Django 4.1.6 on 2023-08-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]