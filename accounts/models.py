# import re
# from django.db import models
# from django.core import validators
# from django.contrib.auth.models import (
#     AbstractBaseUser, PermissionsMixin, UserManager 
# )

# class Usuario(AbstractBaseUser, PermissionsMixin): 
#     username = models.CharField('Usuário', max_length=30, unique=True, validators=[
#             validators.RegexValidator(
#                 re.compile('^[\w.@+-]+$'),
#                 'Informe um nome de usuário válido. '
#                 'Este valor deve conter apenas letras, números '
#                 'e os carecteres: @/./+/-/_.'
#                 ,  'invalid'
#             )
#         ], help_text='Um nome curto que será usado'+
#                     ' para identificá-lo de forma única..'
#     )
#     first_name = models.CharField(max_length=150)
#     email = models.EmailField(max_length=100)
#     is_staff = models.BooleanField('Equipe', default=False)
#     is_active = models.BooleanField('Ativo', default=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     # Criando um gerenciador de usuario para cada user criado
#     Usuario = UserManager()

#     class Meta:
#             verbose_name = 'Usuário'
#             verbose_name_plural = 'Usuários'

#     def __str__(self):
#         return self.name or self.username
    
#     def get_full_name(self):
#         return str(self)

#     def get_short_name(self):
#         return str(self).split(' ')[0]


