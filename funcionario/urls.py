from django.urls import path
from . import views

app_name = 'funcionario'

urlpatterns = [
    path('usuario/', views.DashCreateView, name='dashboard')
#     path('consultas/',),
#     path('consultas/detalhes/',),
#     path('pacientes/'),
#     path('pacientes/prontuario/'),
#     path('meus-dados/'),
#     # urls medico
#     path('agenda/'),
#     path('agenda/atualizar/'),
]