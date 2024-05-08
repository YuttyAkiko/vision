from django import forms
from .models import (Convenio, Paciente, Consulta, Receita, Exame)

class Update_Paciente_Form(forms.ModelForm):

    carteirinha = forms.CharField(max_length=100)

    class Meta:
        model = Paciente
        fields = ('nome_pac','sobrenome_pac','genero_pac','cpf_pac','nasc_pac','tel_pac_1','tel_pac_2','cep_pac','end_pac','bairro_pac',
                  'cidade_pac','email_pac','id_convenio','carteirinha')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_pac'].widget.attrs['readonly'] = True
        self.fields['sobrenome_pac'].widget.attrs['readonly'] = True
        self.fields['genero_pac'].widget.attrs['readonly'] = True
        self.fields['cpf_pac'].widget.attrs['readonly'] = True
        self.fields['nasc_pac'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            if field_name not in ['genero_pac', 'id_convenio','nasc_pac','carteirinha']:
                field.widget.attrs.update({'maxlength': '50', 'size': '60'})

class Delete_Consulta_Form(forms.ModelForm):
    class meta:
        model = Consulta
        fields = ('data_cons','hora_cons','id_paciente','id_medico')

