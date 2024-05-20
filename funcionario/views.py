from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, ListView
from .forms import Update_Funcionario_Form
from django.contrib import messages
from .models import (
    Funcionario, Cargo
)

class GeralView(View):
    def get(self, request, pk):
        
        # Obtém o objeto Funcionario ou retorna 404 se não for encontrado
        funcionario = get_object_or_404(Funcionario, pk=pk)
        username = funcionario.nome_func

        # Obtém o objeto Cargo ou retorna 404 se não for encontrado
        cargo = funcionario.id_cargo

        # Renderiza a página adequada com base no tipo de cargo
        if cargo.tipos_cargo == "ADM":
            return render(request, 'funcionario/dash_adm.html', {'funcionario': funcionario, 'username': username, 'cargo': cargo})
        elif cargo.tipos_cargo == "ATD":
                return render(request, 'funcionario/dash_atend.html', {'funcionario': funcionario, 'username': username, 'cargo': cargo})
        elif cargo.tipos_cargo == "DTR":
                return render(request, 'funcionario/dash_med.html', {'funcionario': funcionario, 'username': username, 'cargo': cargo})
        else:
            messages.add_message(request, messages.INFO, "Perfil de usuário não encontrado.")
            return render(request, 'login.html')

# view generica que atualiza os dados do funcionario
class AtualizarDados(UpdateView):
    model = Funcionario
    form_class = Update_Funcionario_Form
    template_name = 'funcionario/atualizar_dados.html' 

    def get_success_url(self):
        return reverse_lazy('funcionario:geral-list', kwargs={'pk': self.object.pk})
    
class ListarFuncionarios(ListView):
    model = Funcionario
    template_name = 'funcionario/listar_funcionarios.html'
    context_object_name = 'funcionario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        funcionario = GeralView.get(self, self.request, pk=self.kwargs['pk'])
        context['funcionario'] = funcionario
        return context
    