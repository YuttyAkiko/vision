from django.urls import path
from .views import user_login, user_register, password_reset
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', user_login, name='login'),
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', user_register, name='register'),
    path('password-reset/', password_reset, name='password_reset'),

    # Exibir o formulário de solicitação de redefinição de senha
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]