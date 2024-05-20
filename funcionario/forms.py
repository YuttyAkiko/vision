from django import forms
from .models import (Cargo, Funcionario, Especialidade, Medico)

class Update_Funcionario_Form(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome_func','sobrenome_func','genero_func','cpf_func',
                  'nasc_func','tel_func_1','tel_func_2','cep_func','end_func','bairro_func',
                  'cidade_func','email_func')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_func'].widget.attrs['readonly'] = True
        self.fields['sobrenome_func'].widget.attrs['readonly'] = True
        self.fields['genero_func'].widget.attrs['readonly'] = True
        self.fields['cpf_func'].widget.attrs['readonly'] = True
        self.fields['nasc_func'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            if field_name not in ['genero_func', 'id_convenio']:
                field.widget.attrs.update(
                    {'class': 'input-estilizado', 'maxlength': '50', 'size': '60'})
            else:
                field.widget.attrs.update({'class': 'form-select', 'aria-label': 'Disabled select example'})