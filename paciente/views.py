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
            # agendamento = Consulta.objects.filter('filtrar agendamento pela data futura')
            # historico = Consulta.objects.filter('filtrar hitorico pelas datas passadas')
            return render(request, 'dashboard/dash_paciente.html', {'username': username})
        except Paciente.DoesNotExist:
            return render(request, 'login.html')
        
class DeletarConsulta(DeleteView):
    model = Consulta
    template_name = "cancelar_consulta.html"
    success_url = reverse_lazy('dash_paciente.html')