
from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    TIPOS_CARGO = (
        ('Administrador(a)','Administrador(a)'),
        ('Assistente','Assistente'),
        ('Médico(a)','Médico(a)')
    )
    tipos_cargo = models.CharField(max_length=16, choices=TIPOS_CARGO, verbose_name="tipo de cargo")
    nome_cargo = models.CharField(max_length=100, verbose_name="cargo")
    descricao = models.TextField(max_length=500, null=True, verbose_name="descrição")
    entrada = models.TimeField(null=True, verbose_name="entrada")
    saida = models.TimeField(null=True, verbose_name="saída")

class Funcionario(models.Model):
    nome_func = models.CharField(max_length=30, verbose_name="nome")
    # criado campo de usuario na tabela que esta associado a criação de usuario automatica do django
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    sobrenome_func = models.CharField(max_length=50, verbose_name="sobrenome")
    GENEROS_FUNCIONARIO = (
        ('F','Feminino'),
        ('M','Masculino')
    )
    genero_func = models.CharField(max_length=9, choices=GENEROS_FUNCIONARIO, verbose_name="gênero")
    cpf_func = models.PositiveBigIntegerField(verbose_name="cpf")
    nasc_func = models.DateField(auto_now=False, auto_now_add=False, verbose_name="nascimento")
    tel_func_1 = models.IntegerField(verbose_name="Telefone 1")
    tel_func_2 = models.IntegerField(null=True, blank=True, verbose_name="telefone 2")
    cep_func = models.IntegerField(verbose_name="cep")
    end_func = models.CharField(max_length=300, verbose_name="endereço")
    bairro_func = models.CharField(max_length=100, verbose_name="bairro")
    cidade_func = models.CharField(max_length=100, verbose_name="cidade")
    email_func = models.EmailField(max_length=300, verbose_name="email")
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    status_cad_func = models.BooleanField(verbose_name="status de cadastro")

class Medico(models.Model):
    cnpj_med = models.CharField(max_length=12, unique=True, null=True, verbose_name="cnpj")
    crm = models.CharField(max_length=10, unique=True, verbose_name="número CRM")
    id_especialidade = models.ManyToManyField('Especialidade', related_name='Medicos') # Relacionamento Muitos p/ Muitos
    id_funcionario = models.OneToOneField('Funcionario', on_delete= models.CASCADE) # Relacionamento Um p/ Um

class Especialidade(models.Model):
    tipo_especialidade = models.CharField(max_length=30, verbose_name="especialidade")
    valor_consulta = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="valor")

