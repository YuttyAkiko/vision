from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import Update_Funcionario_Form

from .models import (
    Funcionario, Cargo, Medico, Especialidade, #app funcionario
    Paciente # app paciente
)

# funcão que exibirá o nome do usuário/funcionário no header

class DashCreateView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            try:
                user = Funcionario.objects.get(user=current_user)
                username = user.nome_func
                id_cargo = user.id_cargo
                nome_cargo = Cargo.objects.get(user=id_cargo)
                template = loader.get_template('templates/base.html')
                context = {
                    'username': username,
                    'cargo': nome_cargo,
                }
                return HttpResponse(template.render(context, request))
            except user.DoesNotExist:
                pass
        else:
            return HttpResponse(request, 'login.html')


class AtualizarDados(UpdateView):
        form_class = Update_Funcionario_Form()
        template_name = 'atualizar_dados.html'
        
        success_url = reverse_lazy('especialidade_list')


