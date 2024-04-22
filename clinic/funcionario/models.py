from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome_func = models.CharField(max_length=30)
    sobrenome_func = models.CharField(max_length=50)
    GENEROS_FUNCIONARIO = (
        ('Feminino','Feminino'),
        ('Masculino','Masculino')
    )
    genero_func = models.CharField(max_length=9, choices=GENEROS_FUNCIONARIO)
    cpf_func = models.PositiveBigIntegerField()
    nasc_func = models.DateField(auto_now=False, auto_now_add=False)
    tel_func_1 = models.IntegerField()
    tel_func_2 = models.IntegerField(null=True)
    cep_func = models.IntegerField()
    end_func = models.CharField(max_length=300)
    bairro_func = models.CharField(max_length=100)
    cidade_func = models.CharField(max_length=100)
    email_func = models.EmailField(max_length=300)
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    status_cad_func = models.BooleanField()

class Cargo(models.Model):
    TIPOS_CARGO = (
        ('Administrador(a)','Administrador(a)'),
        ('Assistente','Assistente'),
        ('Médico(a)','Médico(a)')
    )
    tipos_cargo = models.CharField(max_length=16, choices=TIPOS_CARGO)
    nome_cargo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500, null=True)
    entrada = models.TimeField(null=True)
    saida = models.TimeField(null=True)

class Medico(models.Model):
    cnpj_med = models.CharField(max_length=12, unique=True, null=True)
    crm = models.CharField(max_length=10, unique=True)
    id_especialidade = models.ManyToManyField('Especialidade', related_name='Medicos') # Relacionamento Muitos p/ Muitos
    id_funcionario = models.OneToOneField('Funcionario', on_delete= models.CASCADE) # Relacionamento Um p/ Um

class Especialidade(models.Model):
    tipo_especialidade = models.CharField(max_length=30)
    valor_consulta = models.DecimalField(max_digits=5, decimal_places=2)


