from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView, ListView
from .models import (
    Convenio, Paciente, Consulta, Receita, Exame
)
from .forms import Update_Paciente_Form, Update_Consulta_Form

# LoginRequiredMixin - função da classe view para solicitar o login do usuario

def Home(request):
    # Página principal da clínica vision
    return render(request, 'institutional/home.html')

def Login(request):
    # Página de Login
    return render(request, 'login.html')

def Agendamento(request):
    # Página de Agendamento
    return render(request, 'agendamento.html')

class GeralView(View):
    # função que irá retornar o objeto paciente
    def get(self, request, pk):
        try:
            paciente, agendamentos, historicos = self.get_queryset(pk)
            return render(request, 'paciente/dash_paciente.html', {
                'paciente': paciente,
                'username': paciente.nome_pac,
                'agendamentos': agendamentos,
                'historicos': historicos
            })
        except Paciente.DoesNotExist:
            return HttpResponseNotFound ("Paciente não encontrado.")
        
    # função que irá retornar separadamente os agendamentos e historicos pelo status da consulta
    def get_queryset(self, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        agendamentos = Consulta.objects.filter(
            Q(id_paciente=paciente, status_cons='Agendada') | # 'Q' adiciona mais de uma condição ao filtro
            Q(id_paciente=paciente, status_cons='Remarcada')
        )
        historicos = Consulta.objects.filter(id_paciente=paciente, status_cons='Concluída')
        return paciente, agendamentos, historicos
        
# class AgendarConsulta():

# view generica que atualiza os dados do paciente
class AtualizarDados(UpdateView):
    model = Paciente
    form_class = Update_Paciente_Form
    template_name = 'paciente/atualizar_dados.html' 

    def get_success_url(self):
        return reverse_lazy('paciente:geral-list', kwargs={'pk': self.get_object().id})
    
# view generica para remarcar consulta
class AlterarConsulta(UpdateView):
    model = Consulta
    form_class = Update_Consulta_Form
    template_name = 'paciente/consulta/alterar_consulta.html'

    # atualiza o status da consulta para remarcada
    def form_valid(self, form):
        consulta = form.save(commit=False)
        consulta.status_cons = 'Remarcada'
        consulta.save()
        return super().form_valid(form)

    def get_success_url(self):
        paciente_pk = self.object.id_paciente.pk
        return reverse_lazy('paciente:geral-list', kwargs={'pk': paciente_pk})

# view generica para cancelar consulta agendada
class CancelarAgendamento(DeleteView):
    model = Consulta
    template_name = 'paciente/dash_paciente.html'

    # função que altera o status de agendada para cancelada
    def post(self, request, pk):
        agendamento = get_object_or_404(Consulta, pk=pk)
        motivo = request.POST.get('motivo', '')

        agendamento.status_cons = 'Cancelada'
        agendamento.observacoes = motivo
        agendamento.save()

        messages.add_message(request, messages.SUCCESS, "Consulta cancelada com sucesso.")
        print(messages)
        return redirect('paciente:geral-list', agendamento.id_paciente.pk)

class ListarHistorico(ListView):
    model = Consulta
    template_name = 'paciente/consulta/listar_historico.html'
    context_object_name = 'historico'  # Nome do objeto que será passado para o template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente, _, historicos = GeralView.get_queryset(self, pk=self.kwargs['pk'])
        context['paciente'] = paciente
        context['historicos'] = historicos
        return context
        
def consulta_por_data(request, pk):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk=pk)
        data_consulta = request.POST.get('data_consulta')
        consulta_por_data = Consulta.objects.filter(data_cons=data_consulta)
        return render(request, 'paciente/consulta/listar_historico.html', {'paciente': paciente,'consulta_por_data': consulta_por_data, 'data_consulta': data_consulta})
    else:
        return render(request, 'paciente/consulta/listar_historico.html')