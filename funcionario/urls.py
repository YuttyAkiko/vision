from django.urls import path
from . import views

app_name = 'funcionario'

urlpatterns = [
    path('geral/<int:pk>', views.GeralView.as_view(), name='geral-list'),
    path('geral/<int:pk>/atualizar-cadastro/', views.AtualizarDados.as_view(), name='atualizar-cadastro'),
    path('geral/<int:pk>/funcionarios/', views.ListarFuncionarios.as_view(), name='listar-funcionarios'),
#     path('consultas/',),
#     path('consultas/detalhes/',),
#     path('pacientes/'),
#     path('pacientes/prontuario/'),
#     path('agenda/'),
#     path('agenda/atualizar/'),
]