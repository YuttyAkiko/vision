from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'paciente'

urlpatterns = [
    path('geral/<int:id>', views.GeralView.as_view(), name='dashboard'),
    path('cancelar-consulta/<int:id>', views.DeletarConsulta.as_view(), name='cancelar-consulta')
]