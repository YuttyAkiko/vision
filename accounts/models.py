# import re
# from django.db import models
# from django.core import validators
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, Group, Permission

# class Usuario(AbstractBaseUser, PermissionsMixin): 
#     username = models.CharField(
#         'Usuário',
#         max_length=30,
#         unique=True,
#         validators=[
#             validators.RegexValidator(
#                 re.compile('^[\w.@+-]+$'),
#                 'Informe um nome de usuário válido. '
#                 'Este valor deve conter apenas letras, números '
#                 'e os caracteres: @/./+/-/_.',
#                 'invalid'
#             )
#         ],
#         help_text='Um nome curto que será usado para identificá-lo de forma única.'
#     )
#     first_name = models.CharField(max_length=150)
#     email = models.EmailField(max_length=100)
#     is_staff = models.BooleanField('Equipe', default=False)
#     is_active = models.BooleanField('Ativo', default=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     # Criando um gerenciador de usuario para cada usuário criado
#     objects = UserManager()

#     groups = models.ManyToManyField(
#         Group,
#         verbose_name='Grupos',
#         blank=True,
#         related_name='usuarios',  # Adicione um related_name exclusivo para evitar conflitos
#         help_text=(
#             'Os grupos a que este usuário pertence. Um usuário receberá todas as permissões '
#             'concedidas a cada um dos seus grupos.'
#         ),
#     )

#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='Permissões de Usuário',
#         blank=True,
#         related_name='usuarios',  # Adicione um related_name exclusivo para evitar conflitos
#         help_text='Permissões específicas para este usuário.',
#         error_messages={
#             'unique': 'Este usuário já possui essa permissão.',
#         },
#     )

#     class Meta:
#         verbose_name = 'Usuário'
#         verbose_name_plural = 'Usuários'

#     def __str__(self):
#         return self.first_name or self.username
    
#     def get_full_name(self):
#         return str(self)

#     def get_short_name(self):
#         return str(self).split(' ')[0]