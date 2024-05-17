from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import Update_Funcionario_Form
from django.contrib import messages
from .models import (
    Funcionario, Cargo
)

# funcão que exibirá o nome do usuário/funcionário no header

class GeralView(View):
    def get(self, request, id):
        
        # Obtém o objeto Funcionario ou retorna 404 se não for encontrado
        funcionario = get_object_or_404(Funcionario, pk=id)
        username = funcionario.nome_func

        # Obtém o objeto Cargo ou retorna 404 se não for encontrado
        cargo = get_object_or_404(Cargo, pk=id)
        nome_cargo = cargo.nome_cargo

        # Renderiza a página adequada com base no tipo de cargo
        if cargo.tipos_cargo == "ADM":
            return render(request, 'dashboard/dash_adm.html', {'username': username, 'cargo': nome_cargo})
        elif cargo.tipos_cargo == "ATD":
                return render(request, 'dashboard/dash_atend.html', {'username': username, 'cargo': nome_cargo})
        elif cargo.tipos_cargo == "DTR":
                return render(request, 'dashboard/dash_med.html', {'username': username, 'cargo': nome_cargo})
        else:
            messages.add_message(request, messages.INFO, "Perfil de usuário não encontrado.")
            return render(request, 'login.html')

class AtualizarDados(UpdateView):
        form_class = Update_Funcionario_Form()
        template_name = 'atualizar_dados.html'
        success_url = reverse_lazy('especialidade_list')

