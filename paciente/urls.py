from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'paciente'

urlpatterns = [
    path('geral/<int:id>', views.GeralView.as_view(), name='dashboard'),
    path('geral/<int:id>/cancelar-consulta/', views.DeletarConsulta.as_view(), name='cancelar-consulta')
]