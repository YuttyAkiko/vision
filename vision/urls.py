from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cadastrar/', views.cadastrar_usuario, name='cadastro')
]

