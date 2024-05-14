from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from paciente.views import Login, Home, Agendamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('login/', Login, name='login'),
    path('agendamento/', Agendamento, name='agendamento'),
    path('funcionario/', include('funcionario.urls', namespace="funcionario")),
    path('paciente/', include('paciente.urls', namespace="paciente"))
]
