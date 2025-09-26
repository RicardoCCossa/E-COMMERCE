from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from users.views import (
    address,
    custom_registration_view,
    custom_login_view,
    custom_password_reset_view,
    profile,
    updateAddress,
)

urlpatterns = [
    # ================================
    # Autenticação
    # ================================
    path('registration/', custom_registration_view, name='custom_registration'),
    path('login/', custom_login_view, name='login'),

    # ================================
    # Perfil e Endereços
    # ================================
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('updateAddress/<int:pk>', updateAddress, name='updateAddress'),

    # ================================
    # Reset de senha (mais completo)
    # ================================
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            email_template_name='users/password_reset_email.html',
            success_url=reverse_lazy('password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page=reverse_lazy('login')),
        name='logout'
    ),
]
