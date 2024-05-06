from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import Update_Funcionario_Form
from .models import (
    Funcionario, Cargo
)

# funcão que exibirá o nome do usuário/funcionário no header

class GeralView(View):
    def get(self, request, id):
        try:
            funcionario = get_object_or_404(Funcionario, pk=id)
            username = funcionario.nome_func
            cargo = get_object_or_404(Cargo, pk=id)
            nome_cargo = cargo.nome_cargo
            return render(request, 'dashboard/dash_adm.html', {'username': username, 'cargo': nome_cargo})
        except Funcionario.DoesNotExist:
            return render(request, 'login.html')

class AtualizarDados(UpdateView):
        form_class = Update_Funcionario_Form()
        template_name = 'atualizar_dados.html'
        
        success_url = reverse_lazy('especialidade_list')

