from django.contrib import admin
from django.urls import path
from accounts import views
from funcionario import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    # URLS´S do app Account

    path('admin/', admin.site.urls),
    # path('cadastrar/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('alterar-senha/', auth_views.PasswordChangeView.as_view(), name='udpate_password'), # Definido uma view padrao do django para alterar a senha
    # path('recuperar-senha/', views.reset_password, name='reset_password'),

    # URLS´S do app Funcionario
    path('dashboard', views.DashCreateView.as_view(), name='dashboard')
]

