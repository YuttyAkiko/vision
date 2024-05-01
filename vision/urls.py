from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from paciente.views import background

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', background, name=background),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('funcionario/', include('funcionario.urls', namespace="funcionario")),
    path('paciente', include('paciente.urls', namespace='paciente'))
]
