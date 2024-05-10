from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from .models import (
    Convenio, Paciente, Consulta, Receita, Exame
)
from .forms import Update_Paciente_Form, Update_Consulta_Form, Delete_Consulta_Form

# LoginRequiredMixin - função da classe view para solicitar o login do usuario

class GeralView(View):
    def get(self, request, pk):
        try:
            paciente = get_object_or_404(Paciente, pk=pk)
            username = paciente.nome_pac
            agendamentos = Consulta.objects.filter(id_paciente=paciente, status_cons='Agendada')
            historicos = Consulta.objects.filter(id_paciente=paciente, status_cons='Concluída')
            return render(request, 'dashboard/dash_paciente.html', {'paciente': paciente, 'username': username, 
            'agendamentos': agendamentos, 'historicos': historicos})
        
        except Paciente.DoesNotExist:
            return render(request, '404.html')
        
# class AgendarConsulta():

class AtualizarDados(UpdateView):
    model = Paciente
    form_class = Update_Paciente_Form
    template_name = 'cadastro/atualizar_dados.html' 

    def get_success_url(self):
        return reverse_lazy('paciente:geral-list',kwargs={'pk': self.get_object().id})

class EditarConsulta(UpdateView):
    model = Consulta
    form_class = Update_Consulta_Form
    template_name = 'consulta/editar.html'

    def get_success_url(self):
        return reverse_lazy('paciente:geral-list',kwargs={'pk': self.get_object().id})

# REVISAAAAAR
class DeletarConsulta(DeleteView):
    model = Consulta
    template_name = "cancelar_consulta.html"

    def get_success_url(self):
        return reverse_lazy('dash_paciente.html',kwargs={'pk': self.get_object().id})
    

        

    
