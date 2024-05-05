# from django.shortcuts import render
# from django.views.decorators.http import require_POST
# from django.contrib.auth.decorators import login_required
# from .models import User

# definindo função de criação de usuario
# @require_POST
# def cadastrar_usuario(request):
#     username = request.POST('input-username')
#     email = request.POST('input-email')
#     senha = request.POST('input-senha')

#     novo_user = User.objects.create_user(username=username, email=email, password=senha)
#     novo_user.save()

def home(request):
    return render(request, 'index.html')

