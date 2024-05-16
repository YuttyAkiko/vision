from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View, UpdateView, DeleteView, TemplateView
from .models import (Convenio, Paciente, Consulta, Receita, Exame)
from .forms import Update_Paciente_Form, Update_Consulta_Form, AddPatientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# LoginRequiredMixin - função da classe view para solicitar o login do usuario


class Home(TemplateView):
    # Página principal da clínica vision
    template_name = 'institutional/home.html'


class Login(TemplateView):
    # Página de Login
    model = Paciente
    template_name = 'login.html'


class Agendamento(TemplateView):
    # Página de Agendamento
    template_name = 'agendamento.html'


class Add_Client(CreateView):
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
                user = User.objects.filter(username=paciente.paciente)
                if user.exists():
                    return HttpResponse("Já existe um usuários com esse username!")

                # Salva o paciente no banco de dados com a informação do usuário associado
                paciente.save()

                # Redireciona para a página de sucesso após o cadastro
                return HttpResponseRedirect('login')
        else:
            # Se a requisição não for do tipo POST, exibe um formulário vazio
            form = AddPatientForm()

        # Renderiza o template 'add.html' com o formulário para exibição
        return render(request, 'cadastro/add.html', {'form': form})


class GeralView(View):
    def get(self, request, pk):
        try:
            paciente = get_object_or_404(Paciente, pk=pk)
            username = paciente.nome_pac
            agendamentos = Consulta.objects.filter(
                id_paciente=paciente, status_cons='Agendada')
            historicos = Consulta.objects.filter(
                id_paciente=paciente, status_cons='Concluída')
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
