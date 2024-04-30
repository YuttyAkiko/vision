# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST
# from django.contrib.auth.views import (
#     LoginView, LogoutView,
#     )
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy
# from django.contrib import messages
# from .models import Usuario

# @require_POST
# def register(request):
#     nome = request.POST('input-nome')
#     username = request.POST('input-username')
#     email = request.POST('input-email')
#     senha = request.POST('input-senha')

#     novo_user = Usuario.objects.create_user(username=username, first_name=nome, email=email, password=senha)
#     novo_user.save()
#     return render(request, 'registration/login.html')    

# class login(LoginView):

#     model = Usuario
#     template_name = 'registration/login.html'

# class Logout(LogoutView):

#     template_name = 'registration/logout.html'

# @login_required
# class UpdatePasswordView(FormView):
#     template_name = "registration/update_password.html"
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy("password_change_done")

#     def form_valid(self, form):
#         user = self.request.user
#         user.set_password(form.cleaned_data['new_password1'])
#         user.save()
#         update_session_auth_hash(self.request, user)
#         messages.success(self.request, 'Sua senha foi alterada com sucesso!')
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, 'Ocorreu um erro ao alterar a senha. Por favor, tente novamente.')
#         return super().form_invalid(form)

# # @login_required
# # def reset_password()


