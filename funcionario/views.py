from django.shortcuts import render, request
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, View

from .models import Funcionario, Cargo, Medico, Especialidade

# funcão que exibirá o nome do usuário/funcionário no header

class DashCreateView(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            usuario = Funcionario.objects.get(user=current_user)
            cargo = Cargo.nome_cargo(usuario)
            template = loader.get_template('templates/base.html')
            context = {
                'username': usuario,
                'cargo': cargo,
            }
            # return HttpResponse(template.render(context, request))
        except usuario.DoesNotExist:
            pass
    # return render(request, 'login.html')



