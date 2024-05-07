from django.contrib import admin
from django.urls import path
# from accounts import views
from paciente.views import PerfilPaciente
from paciente.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cadastrar/', views.cadastrar_usuario, name='cadastro'),
    path('home/', home, name="home"),
    path('perfil-do-paciente/', PerfilPaciente, name="perfil-paciente")
]