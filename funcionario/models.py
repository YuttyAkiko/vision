
from typing import Any
from django.db import models
from django.contrib.auth.models import User
#  from cpf_field.models import CPFField

class Cargo(models.Model):
    TIPOS_CARGO = (
        ('ADM','Administrador(a)'),
        ('ATD','Atendente'),
        ('DTR','Médico(a)')
    )
    tipos_cargo = models.CharField(max_length=16, choices=TIPOS_CARGO, verbose_name="Tipo de Cargo")
    nome_cargo = models.CharField(max_length=100, verbose_name="função")
    descricao = models.TextField(max_length=500, null=True, verbose_name="descrição")
    entrada = models.TimeField(null=True, verbose_name="Horário de Entrada")
    saida = models.TimeField(null=True, verbose_name="Horário de Saída")

    def __str__(self):
        return self.nome_cargo

class Funcionario(models.Model):
    nome_func = models.CharField(max_length=30, verbose_name="nome")
    sobrenome_func = models.CharField(max_length=50, verbose_name="sobrenome")
    GENEROS_FUNCIONARIO = (
        ('F','Feminino'),
        ('M','Masculino')
    )
    genero_func = models.CharField(max_length=9, choices=GENEROS_FUNCIONARIO, verbose_name="gênero")
    cpf_func = models.CharField(max_length=30, verbose_name="CPF")
    nasc_func = models.DateField(auto_now=False, auto_now_add=False, verbose_name="nascimento")
    tel_func_1 = models.IntegerField(verbose_name="telefone 1")
    tel_func_2 = models.IntegerField(null=True, blank=True, verbose_name="telefone 2 (opcional)")
    cep_func = models.IntegerField(verbose_name="CEP")
    end_func = models.CharField(max_length=300, verbose_name="endereço")
    bairro_func = models.CharField(max_length=100, verbose_name="bairro")
    cidade_func = models.CharField(max_length=100, verbose_name="cidade")
    email_func = models.EmailField(max_length=300, verbose_name="e-mail")
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, verbose_name="cargo")
    status_cad_func = models.BooleanField(verbose_name="Ativar Cadastro")

    def __str__(self):
        return f"{self.nome_func} {self.sobrenome_func}"

class Medico(models.Model):
    id_funcionario = models.OneToOneField('Funcionario', on_delete= models.CASCADE, verbose_name="funcionário")
    cnpj_med = models.CharField(max_length=12, unique=True, null=True, verbose_name="CNPJ")
    crm = models.CharField(max_length=10, unique=True, verbose_name="CRM")
    id_especialidade = models.ManyToManyField('Especialidade', related_name='Medicos', verbose_name="especialidade")

    def __str__(self):
        nome_medico = str(self.id_funcionario.nome_func)
        return nome_medico

class Especialidade(models.Model):
    tipo_especialidade = models.CharField(max_length=30, verbose_name="especialidade")
    valor_consulta = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="valor")

    def __str__(self):
        return self.tipo_especialidade

