from django import forms
from .models import (Convenio, Paciente, Consulta, Receita, Exame)

class Update_Paciente_Form(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('tel_pac_1','tel_pac_2','cep_pac','end_pac','bairro_pac','cidade_pac','email_pac')

class Delete_Consulta_Form(forms.ModelForm):
    class meta:
        model = Consulta
        fields = ('data_cons','hora_cons','id_paciente','id_medico')

