import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.views.decorators.http import require_POST

class Criar_Usuario(AbstractBaseUser, PermissionsMixin): 
    user_id     =   models.AutoField(primary_key=True)
    username = models.CharField('Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os carecteres: @/./+/-/_.'
                ,  'invalid'
            )
        ], help_text='Um nome curto que será usado'+
                    ' para identificá-lo de forma única..'
    )

    # # Lista de generos
    # GENERO_CHOICES = (
    #     ('F', 'Feminino')
    #     ('M', 'Masculino')
    #     ('N', 'Nenhuma das opções.')
    # )

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    genero = models.CharField(max_length=30, choices=GENERO_CHOICES)
    cpf = models.IntegerField(max_length=15, unique=True)
    nasc = models.DateField(auto_now=False, auto_now_add=False)
    tel = models.IntegerField()
    endereco = models.CharField()
    bairro = models.CharField()
    cidade = models.CharField()
    email = models.CharField()
    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE)
    # Define usuario como ativo
    is_active = models.BooleanField('Ativo', default=True)

# Criando um gerenciador de usuario para cada user criado
User = UserManager()



