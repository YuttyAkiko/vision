from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('funcionario/', include('medicos.urls', namespace="funcionario")),
]
