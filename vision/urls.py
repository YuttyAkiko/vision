from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas', include('django.contrib.auth.urls')),
    path('funcionario/', include('funcionario.urls', namespace="funcionario")),
    path('paciente/', include('paciente.urls', namespace="paciente"))
]
