# Generated by Django 5.0.4 on 2024-05-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0013_remove_convenio_cpf_titular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='laudo',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='observacoes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='sintomas',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
