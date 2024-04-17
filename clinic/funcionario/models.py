from django.db import models
from django.contrib.auth.models import user
from accounts import User

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True, unique=True)
    cnpj_med = models.CharField(max_length=12, unique=True, null=True)
    crm = models.CharFieldField(max_length=10, unique=True)
    id_especialidade = models.ManyToManyField('Especialidade', related_name='Medicos') # Relacionamento Muitos p/ Muitos
    id_funcionario = models.OneToOneField('Funcionario', on_delete= models.CASCADE) # Relacionamento Um p/ Um

class Especialidade(models.Model):
    id_especialidade = models.AutoField(primary_key=True, unique=True)
    tipo_especialidade = models.CharField(max_length=30)
    valor_consulta = models.DecimalField(max_digits=5, decimal_places=2)

# class Funcionario(models.Model):

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True, unique=True)
    data_cons = models.DateField(auto_now=False, auto_now_add=False)
    hora_cons = models.TimeField()
    id_paciente = models.ForeignKey('Paciente') # Relacionamento Um p/ Muitos
    id_medico = models.ManyToManyField('Medico', related_name='Consulta') # Relacionamento Muitos p/ Muitos
    TIPO_PAG = (
        ('PGO','Pago'),
        ('PDT', 'Pendente')
    )
    tipo_pag_cons = models.CharField(max_length=2, choices=TIPO_PAG)
    status_pag_cons = models.BooleanField() # Select "Yes" ou "No" para o status de pagamento.
    STATUS_CONS = (
        ('CLD', 'Concluída'),
        ('CCD', 'Cancelada'),
        ('PDT', 'Pendente'),
        ('RMD', 'Remarcada'),
    )
    status_cons = models.CharField(max_length=4, choices=STATUS_CONS)
    motivo = models.CharField(max_length=199)
    sintomas = models.TextField(max_length=500, null=True)
    observacoes = models.TextField(max_length=300, null=True)
    laudo = models.CharField(max_length=199, null=True) 
