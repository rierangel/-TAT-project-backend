# Generated by Django 4.1.2 on 2022-11-01 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GaleriaNoticias',
            new_name='GaleriaNoticia',
        ),
        migrations.RenameModel(
            old_name='Noticias',
            new_name='Noticia',
        ),
    ]
