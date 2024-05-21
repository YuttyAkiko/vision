from django import forms
from .models import (Cargo, Funcionario, Especialidade, Medico)

class Update_Funcionario_Form(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome_func','sobrenome_func','genero_func','cpf_func',
                'nasc_func','tel_func','cep_func','end_func','bairro_func',
                'cidade_func','email_func','status_cad_func')