from django import forms
from .models import (Convenio, Paciente, Consulta, Receita, Exame)
from funcionario.models import (Medico, Especialidade, Funcionario)

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput, label='Senha')
    class Meta:
        model = Paciente
        fields = ('username', 'email_pac', 'password')

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome_pac', 'sobrenome_pac', 'genero_pac', 'cpf_pac', 'nasc_pac', 'tel_pac_1', 'tel_pac_2',
                'cep_pac', 'end_pac', 'bairro_pac', 'cidade_pac', 'id_convenio', 'num_carteirinha')

class AddAgendaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('id_especialidade', 'data_cons', 'hora_cons', 'id_medico')

class Update_Paciente_Form(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome_pac', 'sobrenome_pac', 'genero_pac', 'cpf_pac', 'nasc_pac', 'tel_pac_1', 'tel_pac_2',
                'cep_pac', 'end_pac', 'bairro_pac', 'cidade_pac', 'email_pac', 'id_convenio', 'num_carteirinha')

    # adicionando readonly aos campos nao editaveis
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_pac'].widget.attrs['readonly'] = True
        self.fields['sobrenome_pac'].widget.attrs['readonly'] = True
        self.fields['genero_pac'].widget.attrs['readonly'] = True
        self.fields['cpf_pac'].widget.attrs['readonly'] = True
        self.fields['nasc_pac'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            if field_name not in ['genero_pac', 'id_convenio']:
                field.widget.attrs.update(
                    {'class': 'input-estilizado', 'maxlength': '50', 'size': '60'})
            else:
                field.widget.attrs.update({'class': 'custom-select'})


class Update_Consulta_Form(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('data_cons', 'hora_cons', 'id_especialidade', 'id_medico')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['id_especialidade', 'id_medico']:
                field.widget.attrs.update(
                    {'class': 'input-estilizado', 'maxlength': '30', 'size': '40'})
            else:
                field.widget.attrs.update(
                    {'class': 'form-select', 'aria-label': 'Default select example'})
