# Generated by Django 5.0.4 on 2024-05-13 17:52

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_func',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
    ]