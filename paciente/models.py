from django.db import models
from django.contrib.auth.models import User
from funcionario.models import Medico

class Convenio(models.Model):
  nome_convenio = models.CharField(max_length=50, null=True)

  def __str__(self):
    return self.nome_convenio

class Paciente(models.Model):
  nome_pac = models.CharField(max_length=30, verbose_name="nome")
  sobrenome_pac = models.CharField(max_length=50, verbose_name="sobrenome")
  GENERO_PACIENTE = (
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino')
  )
  genero_pac = models.CharField(max_length=10, choices=GENERO_PACIENTE, verbose_name="gênero")
  cpf_pac = models.PositiveBigIntegerField(verbose_name="CPF")
  nasc_pac  = models.DateField(auto_now=False, auto_now_add=False, verbose_name="nascimento")
  tel_pac_1 = models.IntegerField(verbose_name="Telefone 1")
  tel_pac_2 = models.IntegerField(null=True, blank=True, verbose_name="Telefone 2 (Opcional)")
  cep_pac = models.IntegerField(verbose_name="CEP")
  end_pac = models.CharField(max_length=300, verbose_name="endereço")
  bairro_pac = models.CharField(max_length=100, verbose_name="bairro")
  cidade_pac = models.CharField(max_length=100, verbose_name="cidade")
  email_pac = models.EmailField(max_length=300, verbose_name="e-mail")
  status_cad_pac = models.BooleanField(verbose_name="ativar cadastro")
  id_convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE, blank=True, verbose_name="convênio") # Relacionamento (1,n)
  num_carteirinha = models.IntegerField(blank=True, default=0)

  def __str__(self):
    return self.nome_pac
  
class Consulta(models.Model):
    data_cons = models.DateField(auto_now=False, auto_now_add=False)
    hora_cons = models.TimeField()
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE) # Relacionamento (1,n)
    id_medico = models.ForeignKey(Medico, related_name='Consulta', on_delete=models.CASCADE, default=0) # Relacionamento (1,n)
    TIPOS_PAGAMENTO = (
        ('Cartão','Cartão'),
        ('Dinheiro','Dinheiro'),
        ('Pix','Pix')
    )
    tipo_pag_cons = models.CharField(max_length=10, choices=TIPOS_PAGAMENTO)
    STATUS_PAGAMENTO = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente')
    )
    status_pag_cons = models.CharField(max_length=10, choices=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.
    STATUS_CONSULTA = (
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
        ('Pendente', 'Pendente'),
        ('Remarcada', 'Remarcada'),
    )
    status_cons = models.CharField(max_length=10, choices=STATUS_CONSULTA)
    motivo = models.CharField(max_length=199)
    sintomas = models.TextField(max_length=500, null=True, blank=True)
    observacoes = models.TextField(max_length=500, null=True, blank=True)
    laudo = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['data_cons', 'hora_cons']
  
class Receita(models.Model):
  id_consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE) # Relacionamento (1,n)
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
  id_consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE)
  tipo_exame = models.CharField(max_length=30)
  valor_exame = models.FloatField()
  TIPOS_PAGAMENTO = (
        ('Cartão','Cartão'),
        ('Dinheiro','Dinheiro'),
        ('Pix','Pix')
    )
  tipo_pag_ex = models.CharField(max_length=10, choices=TIPOS_PAGAMENTO)
  STATUS_PAGAMENTO = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente')
    )
  status_pag_ex = models.CharField(max_length=10, choices=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.