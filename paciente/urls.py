from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'paciente'

urlpatterns = [
    path('geral/<int:pk>', views.GeralView.as_view(), name='geral-list'),
    path('geral/<int:pk>/atualizar-cadastro/', views.AtualizarDados.as_view(), name='atualizar-cadastro'),
    path('geral/<int:pk>/alterar-consulta/', views.AlterarConsulta.as_view(), name='alterar-consulta'),
    path('geral/<int:pk>/cancelar-consulta/', views.CancelarAgendamento.as_view(), name='cancelar-consulta'),
    path('geral/<int:pk>/cancelar-consulta/', views.CancelarAgendamento.as_view(), name='listar-consulta'),
    path('geral/<int:pk>/historico/', views.ListarHistorico.as_view(), name='listar-historico'),
    path('geral/<int:pk>/historico-por-data/', views.historico_por_data, name='historico-por-data'),
]