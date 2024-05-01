from django.contrib import admin
from django.urls import path
from accounts import views
from paciente.views import background

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', background, name=background),
    # path('cadastrar/', views.cadastrar_usuario, name='cadastro')
]

