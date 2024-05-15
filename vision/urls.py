from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from paciente.views import Login, Home, Agendamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('agendamento/', Agendamento.as_view(), name='agendamento'),
    path('funcionario/', include('funcionario.urls', namespace="funcionario")),
    path('paciente/', include('paciente.urls', namespace="paciente"))
]
