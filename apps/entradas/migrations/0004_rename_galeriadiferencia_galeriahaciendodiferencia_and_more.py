# Generated by Django 4.1.2 on 2022-11-01 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0003_congreso_diferencia_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GaleriaDiferencia',
            new_name='GaleriaHaciendoDiferencia',
        ),
        migrations.RenameModel(
            old_name='Diferencia',
            new_name='HaciendoDiferencia',
        ),
    ]
