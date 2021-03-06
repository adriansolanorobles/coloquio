# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('edad', models.CharField(max_length=2)),
                ('celular', models.CharField(max_length=10)),
                ('trabajas_en_educacion', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('institucion_de_procedencia', models.CharField(blank=True, max_length=255, null=True)),
                ('preescolar', models.NullBooleanField(default=False)),
                ('primaria', models.NullBooleanField(default=False)),
                ('secundaria', models.NullBooleanField(default=False)),
                ('media_superior', models.NullBooleanField(default=False)),
                ('superior', models.NullBooleanField(default=False)),
                ('posgrado', models.NullBooleanField(default=False)),
                ('no_formal', models.NullBooleanField(default=False)),
                ('ocupacion', models.CharField(blank=True, max_length=255, null=True)),
                ('nombramiento', models.CharField(blank=True, max_length=255, null=True)),
                ('te_gustaria_recibir_informacion', models.BooleanField()),
                ('ceated', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
