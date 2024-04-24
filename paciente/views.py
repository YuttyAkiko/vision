from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def PerfilPaciente(request):
  return render(request, "paciente/perfil-paciente.html")