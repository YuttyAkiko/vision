from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'paciente'

urlpatterns = [
    path('cadastro/', views.client_register, name="cadastro"),
    path('geral/<int:pk>', views.client_profile, name='geral-list'),
    path('geral/<int:pk>/atualizar-cadastro/', views.client_update, name='atualizar-cadastro'),
    path('geral/<int:pk>/editar-consulta/', views.agenda_update, name='editar-consulta'),
    path('geral/<int:pk>/cancelar-consulta/', views.agenda_delete, name='cancelar-consulta'),
    path('geral/<int:pk>/agendamento/', views.agenda_register, name='agenda'),
]   