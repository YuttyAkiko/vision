import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager, User
)

class User(AbstractBaseUser, PermissionsMixin): 
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
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=16, unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)

# Criando um gerenciador de usuario para cada user criado
User = UserManager()



