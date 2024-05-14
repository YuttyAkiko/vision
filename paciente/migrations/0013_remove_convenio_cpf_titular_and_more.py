# Generated by Django 5.0.2 on 2024-05-10 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0006_alter_funcionario_status_cad_func'),
        ('paciente', '0012_alter_consulta_options_alter_convenio_nome_convenio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convenio',
            name='cpf_titular',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='num_carteirinha',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='titular',
        ),
        migrations.AddField(
            model_name='paciente',
            name='num_carteirinha',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='id_medico',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='bairro_pac',
            field=models.CharField(max_length=100, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cep_pac',
            field=models.IntegerField(verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade_pac',
            field=models.CharField(max_length=100, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf_pac',
            field=models.PositiveBigIntegerField(verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email_pac',
            field=models.EmailField(max_length=300, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='end_pac',
            field=models.CharField(max_length=300, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero_pac',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=10, verbose_name='gênero'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='id_convenio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.convenio', verbose_name='convênio'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nasc_pac',
            field=models.DateField(verbose_name='nascimento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome_pac',
            field=models.CharField(max_length=30, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sobrenome_pac',
            field=models.CharField(max_length=50, verbose_name='sobrenome'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='status_cad_pac',
            field=models.BooleanField(verbose_name='ativar Cadastro'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tel_pac_1',
            field=models.IntegerField(verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tel_pac_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefone 2 (Opcional)'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_medico',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Consulta', to='funcionario.medico'),
        ),
    ]