# Generated by Django 5.1.6 on 2025-02-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinos',
            name='etiqueta',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vinos',
            name='variedad',
            field=models.CharField(max_length=30),
        ),
    ]
