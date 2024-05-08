from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, DeleteView
from .models import (
    Convenio, Paciente, Consulta, Receita, Exame
)

class GeralView(View):
    def get(self, request, id):
        try:
            paciente = get_object_or_404(Paciente, pk=id)
            username = paciente.nome_pac
            agendamentos = Consulta.objects.filter(nome_pac=username, status_cons='Pendente').values()


            historico = Consulta.objects.filter()
            return render(request, 'dashboard/dash_paciente.html', {'username': username, 
            'agendamento': agendamento, })
        
        except Paciente.DoesNotExist:
            return render(request, 'login.html')


# REVISAAAAAR
class DeletarConsulta(DeleteView):
    model = Consulta
    template_name = "cancelar_consulta.html"

    def get_success_url(self):
        return reverse_lazy('dash_paciente.html',kwargs={'pk': self.get_object().id})
    
