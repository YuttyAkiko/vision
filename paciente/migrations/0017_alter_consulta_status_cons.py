# Generated by Django 5.0.4 on 2024-05-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0016_alter_consulta_id_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='status_cons',
            field=models.CharField(choices=[('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')], max_length=10),
        ),
    ]