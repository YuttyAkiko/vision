# Generated by Django 5.0.4 on 2024-05-06 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0006_alter_paciente_tel_pac_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id_convenio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.convenio'),
        ),
    ]
