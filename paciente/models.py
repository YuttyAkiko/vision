from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
  # id_paciente = models.AutoField(primary_key=True, unique=True)
  nome_pac = models.CharField(max_length=30)
  sobrenome_pac = models.CharField(max_length=50)
  GENERO_PACIENTE = (
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino')
  )
  genero_pac = models.CharField(max_length=9, choices=GENERO_PACIENTE)
  cpf_pac = models.PositiveBigIntegerField()
  nasc_pac  = models.DateField(auto_now=False, auto_now_add=False)
  tel_pac_1 = models.IntegerField()
  tel_pac_2 = models.IntegerField(null=True)
  cep_pac = models.IntegerField()
  end_pac = models.CharField(max_length=300)
  bairro_pac = models.CharField(max_length=100)
  cidade_pac = models.CharField(max_length=100)
  email_func = models.EmailField(max_length=300)
  id_convenio = models.ForeignKey('Convenio') # Relacionamento (1,n)
  status_cad_pac = models.BooleanField()
  
class Convenio(models.Model):
  # id_convenio = models.AutoField(primary_key=True, unique=True)
  num_carteirinha = models.IntegerField(null=True)
  nome_convenio = models.CharField(max_length=50, null=True)
  titular = models.CharField(max_length=50, null=True)
  cpf_titular = models.models.PositiveIntegerField()
  
class Consulta(models.Model):
    # id_consulta = models.AutoField(primary_key=True, unique=True)
    data_cons = models.DateField(auto_now=False, auto_now_add=False)
    hora_cons = models.TimeField()
    id_paciente = models.ForeignKey('Paciente') # Relacionamento (1,n)
    id_medico = models.ManyToManyField('Medico', related_name='Consulta') # Relacionamento (n,n)
    TIPOS_PAGAMENTO = (
        ('Cartão','Cartão'),
        ('Dinheiro','Dinheiro'),
        ('Pix','Pix')
    )
    tipo_pag_cons = models.CharField(max_length=3, choices=TIPOS_PAGAMENTO)
    STATUS_PAGAMENTO = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente')
    )
    status_pag_cons = models.CharField(max_length=2, choices=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.
    STATUS_CONSULTA = (
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
        ('Pendente', 'Pendente'),
        ('Remarcada', 'Remarcada'),
    )
    status_cons = models.CharField(max_length=4, choices=STATUS_CONSULTA)
    motivo = models.CharField(max_length=199)
    sintomas = models.TextField(max_length=500, null=True)
    observacoes = models.TextField(max_length=500, null=True)
    laudo = models.TextField(max_length=500, null=True)
    
class Receita(models.Model):
  # id_receita = models.AutoField(primary_key=True, unique=True)
  id_consulta = models.ForeignKey('Consulta') # Relacionamento (1,n)
  data_rec = models.DateTimeField(auto_now_add=True)
  L_esf_OD = models.CharField(max_length=30, null=True)
  L_esf_OE = models.CharField(max_length=30, null=True)
  L_cil_OD = models.CharField(max_length=30, null=True)
  L_cil_OE = models.CharField(max_length=30, null=True)
  L_eixo_OD = models.CharField(max_length=30, null=True)
  L_eixo_OE = models.CharField(max_length=30, null=True)
  L_dp_OD = models.CharField(max_length=30, null=True)
  L_dp_OE = models.CharField(max_length=30, null=True)
  P_esf_OD = models.CharField(max_length=30, null=True)
  P_esf_OE = models.CharField(max_length=30, null=True)
  P_cil_OD = models.CharField(max_length=30, null=True)
  P_cil_OE = models.CharField(max_length=30, null=True)
  P_eixo_OD = models.CharField(max_length=30, null=True)
  P_eixo_OE = models.CharField(max_length=30, null=True)
  P_dp_OD = models.CharField(max_length=30, null=True)
  P_dp_OE = models.CharField(max_length=30, null=True)
  
class Exame(models.Model):
  # id_exame = models.AutoField(primary_key=True, unique=True)
  id_consulta = models.ForeignKey('Consulta', on_delete=True)
  tipo_exame = models.CharField(max_length=30)
  valor_exame = models.FloatField()
  TIPOS_PAGAMENTO = (
        ('Cartão','Cartão'),
        ('Dinheiro','Dinheiro'),
        ('Pix','Pix')
    )
  tipo_pag_ex = models.CharField(max_length=3, choices=TIPOS_PAGAMENTO)
  STATUS_PAGAMENTO = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente')
    )
  status_pag_ex = models.CharField(max_length=2, choices=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.