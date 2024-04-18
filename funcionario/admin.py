from django.contrib import admin
from .models import Funcionario, Cargo, Medico, Especialidade

admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Medico)
admin.site.register(Especialidade)