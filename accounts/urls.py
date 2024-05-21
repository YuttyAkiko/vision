
from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.login, name='login'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('registro/', views.register, name='register'),
    path('sair/', views.logout, name='logout'),
    path('recuperar-senha/',
        views.password_reset_request,
        name='password_reset'
    ),
    path('recuperar-senha-ok/', 
        auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path('recuperar-senha-completo/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password/password_reset_complete.html'
            ),
            name='password_reset_complete',
    ),
    path('recuperar-senha-confirmar/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_confirm.html',
        success_url=reverse_lazy("accounts:password_reset_complete")
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_confirm',
        views.password_reset_request,
        name="password_reset"
    )

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

""" from django.urls import path
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
] """