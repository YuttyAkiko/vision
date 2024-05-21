# Generated by Django 5.0.4 on 2024-05-20 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos_cargo', models.CharField(choices=[('ADM', 'Administrador(a)'), ('ATD', 'Atendente'), ('DTR', 'Médico(a)')], max_length=16)),
                ('nome_cargo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=2000, null=True)),
                ('entrada', models.TimeField(null=True)),
                ('saida', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_especialidade', models.CharField(max_length=30)),
                ('valor_consulta', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_func', models.CharField(max_length=30)),
                ('sobrenome_func', models.CharField(max_length=50)),
                ('genero_func', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=9)),
                ('cpf_func', models.CharField(max_length=30, verbose_name='CPF')),
                ('nasc_func', models.DateField()),
                ('tel_func_1', models.CharField(max_length=30)),
                ('tel_func_2', models.CharField(blank=True, max_length=30, null=True)),
                ('cep_func', models.CharField(max_length=30)),
                ('end_func', models.CharField(max_length=300)),
                ('bairro_func', models.CharField(max_length=100)),
                ('cidade_func', models.CharField(max_length=100)),
                ('email_func', models.EmailField(max_length=300)),
                ('status_cad_func', models.BooleanField(verbose_name='Ativar Cadastro')),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj_med', models.CharField(max_length=12, null=True, unique=True)),
                ('crm', models.CharField(max_length=10, unique=True)),
                ('id_especialidade', models.ManyToManyField(related_name='Medicos', to='funcionario.especialidade')),
                ('id_funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario')),
            ],
        ),
    ]
