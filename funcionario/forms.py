from django import forms
from .models import (Cargo, Funcionario, Especialidade, Medico)

class Update_Funcionario_Form(forms.modelForms):
    class Meta:
        model = Funcionario
        fields = ('nome','nasc')