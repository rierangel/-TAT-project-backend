# Generated by Django 4.1.2 on 2022-11-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0004_rename_galeriadiferencia_galeriahaciendodiferencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='congreso',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='haciendodiferencia',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
