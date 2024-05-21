from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('conta/', include('accounts.urls', namespace="accounts")),
    path('funcionario/', include('funcionario.urls', namespace="funcionario")),
    path('paciente/', include('paciente.urls', namespace="paciente"))
    # path('login/', Login.as_view(), name='login'),
    # path('agendamento/', Agendamento.as_view(), name='agenda'),
]
