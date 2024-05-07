from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, "/templates/institucional/home.html")

def PerfilPaciente(request):
  return render(request, "/templates/paciente/dados_perfil_pac.html")