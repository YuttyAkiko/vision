# Generated by Django 5.0.4 on 2024-05-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='status_cad_pac',
            field=models.BooleanField(verbose_name='Ativar Cadastro'),
        ),
    ]
