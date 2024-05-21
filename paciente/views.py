from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView, ListView
from django.urls import reverse_lazy, reverse
from django.db import IntegrityError
from .forms import Update_Paciente_Form, Update_Consulta_Form, AddPatientForm, AddAgendaForm
from .models import (Paciente, Consulta)
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

# LoginRequiredMixin - função da classe view para solicitar o login do usuario

class Home(TemplateView):
    # Página principal da clínica vision
    template_name = 'institutional/home.html'
    
class ClientGeralView(LoginRequiredMixin, DetailView):

    def get(self, request, pk):
        try:
            paciente = get_object_or_404(Paciente, pk=pk)
            username = paciente.nome_pac + " " + paciente.sobrenome_pac
            agendamentos = Consulta.objects.filter(
                id_paciente=paciente, status_cons='Agendada')
            historicos = Consulta.objects.filter(
                id_paciente=paciente, status_cons='Concluída')
            return render(request, 'dashboard/dash_paciente.html', {'paciente': paciente, 'username': username,
                                                                    'agendamentos': agendamentos, 'historicos': historicos})

        except Paciente.DoesNotExist:
            return render(request, '404.html')
    
class ClientCreateView(LoginRequiredMixin, CreateView):
    
    model = Paciente
    template_name = 'accounts/resgister.html'
    form_class = AddPatientForm
    success_url = reverse_lazy('paciente:geral-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClientUpdateView(LoginRequiredMixin, UpdateView):
    # Atualização dos dados cadastrais do paciente
    model = Paciente
    login_url = reverse_lazy('accounts:login')
    template_name = 'cadastro/atualizar_dados.html'
    form_class = Update_Paciente_Form
    success_url = reverse_lazy('paciente:geral-list')

    def get_object(self):
        user = self.request.user
        try:
            return Paciente.objects.get(user=user)
        except Paciente.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AgendaCreateView(LoginRequiredMixin, CreateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'agenda/add_agenda.html'
    form_class = AddAgendaForm
    success_url = reverse_lazy('paciente:geral-list')
    
    def form_valid(self, form):
        try:
            form.instance.client = Paciente.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Você não pode marcar esta consulta')
                return HttpResponseRedirect(reverse_lazy('agenda/add_agenda.html'))
        except Paciente.DoesNotExist:
            messages.warning(self.request, 'Complete seu cadastro')
            return HttpResponseRedirect(reverse_lazy('paciente:client_create'))
        messages.info(self.request, 'Consulta marcada com sucesso!')
        return HttpResponseRedirect(reverse_lazy('paciente:agenda_list'))
    
class AgendaUpdateView(LoginRequiredMixin, UpdateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'consulta/editar-consulta.html'
    form_class = Update_Consulta_Form
    success_url = reverse_lazy('funcionario:agenda_lista')
    
    def form_valid(self, form):
        form.instance.client = Consulta.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('paciente:agenda_list')
    template_name = 'consulta/cancelar-consulta.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('paciente:agenda_list')
    
    def post(self, request, pk):
        consulta = get_object_or_404(Consulta, pk=pk)
        motivo = request.POST.get('motivo', '')

        consulta.status_cons = 'Cancelada'
        consulta.observacoes = motivo
        consulta.save()

        return redirect('paciente:geral-list', consulta.id_paciente.pk)


class AgendaListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'paciente/consulta_list.html'

    def get_queryset(self):
        user=self.request.user
        try:
            paciente = Paciente.objects.get(user=user)
        except Paciente.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        try:
            consultas = Consulta.objects.filter(paciente=paciente).order_by('-pk')
        except Consulta.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        return consultas

client_profile = ClientGeralView.as_view()
client_register = ClientCreateView.as_view()
client_update = ClientUpdateView.as_view()
agenda_list = AgendaListView.as_view()
agenda_register = AgendaCreateView.as_view()
agenda_update = AgendaUpdateView.as_view()
agenda_delete = AgendaDeleteView.as_view()


""" class Add_Client(LoginRequiredMixin, CreateView):
    
    model = Paciente
    template_name = 'cadastro/add.html'
    form_class = AddPatientForm
    success_url = reverse_lazy('paciente:geral-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) """

""" class AtualizarDados(UpdateView):
    model = Paciente
    form_class = Update_Paciente_Form
    template_name = 'cadastro/atualizar_dados.html'

    def get_success_url(self):
        return reverse_lazy('paciente:geral-list', kwargs={'pk': self.get_object().id}) """
        

""" class EditarConsulta(UpdateView):
    model = Consulta
    form_class = Update_Consulta_Form
    template_name = 'consulta/editar-consulta.html'

    def get_success_url(self):
        paciente_pk = self.object.id_paciente.pk
        return reverse_lazy('paciente:geral-list', kwargs={'pk': paciente_pk}) """


""" class CancelarConsulta(DeleteView):
    model = Consulta
    template_name = 'consulta/cancelar-consulta.html'

    def post(self, request, pk):
        consulta = get_object_or_404(Consulta, pk=pk)
        motivo = request.POST.get('motivo', '')

        consulta.status_cons = 'Cancelada'
        consulta.observacoes = motivo
        consulta.save()

        return redirect('paciente:geral-list', consulta.id_paciente.pk) """

""" class Agendamento(CreateView):
    model = Consulta
    form_class = AddAgendaForm
    template_name = 'agenda/agenda.html'

    def post(request):
        if request.method == "POST":
            form = AddAgendaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("agenda/sucess.html"))
        else:
            form = AddAgendaForm()

        return render(request, 'agenda/agenda.html', {'form': form}) """
    




