# Generated by Django 5.1.6 on 2025-02-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_vinos_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinos',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True),
        ),
    ]
