from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def background(request):
    return render(request, 'template/background.html')
=======
# Create your views here.

def PerfilPaciente(request):
  return render(request, "paciente/perfil-paciente.html")
>>>>>>> 843f08f721acf512617ef2838ffa4f78c6c67f05
