# Generated by Django 5.0.4 on 2024-05-14 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_convenio', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cons', models.DateField()),
                ('hora_cons', models.TimeField()),
                ('tipo_pag_cons', models.CharField(choices=[('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], max_length=10)),
                ('status_pag_cons', models.CharField(choices=[('Pago', 'Pago'), ('Pendente', 'Pendente')], max_length=10)),
                ('status_cons', models.CharField(choices=[('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')], max_length=10)),
                ('motivo', models.CharField(max_length=199)),
                ('sintomas', models.TextField(blank=True, max_length=2000, null=True)),
                ('observacoes', models.TextField(blank=True, max_length=2000, null=True)),
                ('laudo', models.TextField(blank=True, max_length=2000, null=True)),
                ('id_especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='funcionario.especialidade')),
                ('id_medico', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Consulta', to='funcionario.medico')),
            ],
            options={
                'ordering': ['data_cons', 'hora_cons'],
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_exame', models.CharField(max_length=30)),
                ('valor_exame', models.FloatField()),
                ('tipo_pag_ex', models.CharField(choices=[('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], max_length=10)),
                ('status_pag_ex', models.CharField(choices=[('Pago', 'Pago'), ('Pendente', 'Pendente')], max_length=10)),
                ('id_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pac', models.CharField(max_length=30, verbose_name='nome')),
                ('sobrenome_pac', models.CharField(max_length=50, verbose_name='sobrenome')),
                ('genero_pac', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=10, verbose_name='gênero')),
                ('cpf_pac', models.CharField(max_length=30, verbose_name='CPF')),
                ('nasc_pac', models.DateField(verbose_name='nascimento')),
                ('tel_pac_1', models.CharField(max_length=30, verbose_name='Telefone 1')),
                ('tel_pac_2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone 2 (Opcional)')),
                ('cep_pac', models.CharField(max_length=30, verbose_name='CEP')),
                ('end_pac', models.CharField(max_length=300, verbose_name='endereço')),
                ('bairro_pac', models.CharField(max_length=100, verbose_name='bairro')),
                ('cidade_pac', models.CharField(max_length=100, verbose_name='cidade')),
                ('email_pac', models.EmailField(max_length=300, verbose_name='e-mail')),
                ('status_cad_pac', models.BooleanField(verbose_name='ativar cadastro')),
                ('num_carteirinha', models.IntegerField(blank=True, default=0, verbose_name='carteirinha')),
                ('id_convenio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.convenio', verbose_name='convênio')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente'),
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_rec', models.DateTimeField(auto_now_add=True)),
                ('L_esf_OD', models.CharField(max_length=30, null=True)),
                ('L_esf_OE', models.CharField(max_length=30, null=True)),
                ('L_cil_OD', models.CharField(max_length=30, null=True)),
                ('L_cil_OE', models.CharField(max_length=30, null=True)),
                ('L_eixo_OD', models.CharField(max_length=30, null=True)),
                ('L_eixo_OE', models.CharField(max_length=30, null=True)),
                ('L_dp_OD', models.CharField(max_length=30, null=True)),
                ('L_dp_OE', models.CharField(max_length=30, null=True)),
                ('P_esf_OD', models.CharField(max_length=30, null=True)),
                ('P_esf_OE', models.CharField(max_length=30, null=True)),
                ('P_cil_OD', models.CharField(max_length=30, null=True)),
                ('P_cil_OE', models.CharField(max_length=30, null=True)),
                ('P_eixo_OD', models.CharField(max_length=30, null=True)),
                ('P_eixo_OE', models.CharField(max_length=30, null=True)),
                ('P_dp_OD', models.CharField(max_length=30, null=True)),
                ('P_dp_OE', models.CharField(max_length=30, null=True)),
                ('id_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.consulta')),
            ],
        ),
    ]
