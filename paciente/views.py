from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, View, DeleteView, TemplateView
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
    
class GeralView(View):
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
        
class Add_Client(LoginRequiredMixin, CreateView):
    
    model = Paciente
    template_name = 'cadastro/add.html'
    form_class = AddPatientForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

""" class Add_Client(CreateView):
    # Quando o cadastro é realizado com sucesso, o cliente é redirecionado para a página de login.
    model = Paciente
    form_class = AddPatientForm
    template_name = "cadastro/add.html"

    def add(request):
        if request.method == 'POST':  # Verifica se a requisição é do tipo POST
            # Cria uma instância do formulário com os dados submetidos
            form = AddPatientForm(request.POST)
            if form.is_valid():  # Verifica se os dados do formulário são válidos

                # Salva os dados do formulário no objeto Paciente, mas não no banco de dados
                paciente = form.save(commit=False)

                # Cria um novo usuário do Django com os dados fornecidos
                user = User.objects.create_user(
                    username=paciente.email_pac, email=paciente.email_pac, password=form.cleaned_data['password'])

                # Associa o paciente ao usuário criado
                paciente.user = user

                # Verifica se o usuário já existe
                user = User.objects.filter(username=paciente.paciente, cpf=paciente.cpf_pac)
                if user.exists():
                    return HttpResponse("Já existe um usuários com esse username!")

                # Salva o paciente no banco de dados com a informação do usuário associado
                paciente.save()

                # Redireciona para a página de sucesso após o cadastro
                return redirect('accounts:login')
        else:
            # Se a requisição não for do tipo POST, exibe um formulário vazio
            form = AddPatientForm()

        # Renderiza o template 'add.html' com o formulário para exibição
        return render(request, 'cadastro/add.html', {'form': form}) """

# class AgendarConsulta():


class AtualizarDados(UpdateView):
    model = Paciente
    form_class = Update_Paciente_Form
    template_name = 'cadastro/atualizar_dados.html'

    def get_success_url(self):
        return reverse_lazy('paciente:geral-list', kwargs={'pk': self.get_object().id})


class EditarConsulta(UpdateView):
    model = Consulta
    form_class = Update_Consulta_Form
    template_name = 'consulta/editar-consulta.html'

    def get_success_url(self):
        paciente_pk = self.object.id_paciente.pk
        return reverse_lazy('paciente:geral-list', kwargs={'pk': paciente_pk})


class CancelarConsulta(DeleteView):
    model = Consulta
    template_name = 'consulta/cancelar-consulta.html'

    def post(self, request, pk):
        consulta = get_object_or_404(Consulta, pk=pk)
        motivo = request.POST.get('motivo', '')

        consulta.status_cons = 'Cancelada'
        consulta.observacoes = motivo
        consulta.save()

        return redirect('paciente:geral-list', consulta.id_paciente.pk)





""" class Login(TemplateView):
    # Página de Login
    model = Paciente
    template_name = 'login.html'

    def login(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('geral-list')  # Redireciona para a página inicial ou outra página desejada
                else:
                    messages.error(request, 'E-mail ou senha inválidos!')
        else:
            print('erro')
            form = LoginForm()
        return render(request, 'login.html', {'form': form}) """

class Agendamento(CreateView):
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

        return render(request, 'agenda/agenda.html', {'form': form})
    
class ClienteCreateView(LoginRequiredMixin ,CreateView):
    
    model = Paciente
    template_name = 'clientes/cadastro.html'
    fields = ['nome_pac', 'sobrenome_pac', 'genero_pac', 'cpf_pac', 'nasc_pac', 'tel_pac_1', 'tel_pac_2',
                'cep_pac', 'end_pac', 'bairro_pac', 'cidade_pac', 'id_convenio', 'num_carteirinha', 'email_pac']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




