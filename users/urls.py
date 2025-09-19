from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    address,
    custom_registration_view,
    custom_login_view,
    custom_password_reset_view,
    profile,
)

urlpatterns = [
    # ================================
    # Autenticação
    # ================================
    path('registration/', custom_registration_view, name='custom_registration'),
    path("login/", custom_login_view, name="login"),
    # ================================
    # Reset de senha (mais completo)
    # ================================
   path("password-reset/", custom_password_reset_view, name="my_password_reset"),
   path('profile/', profile, name='profile'),
   path('address/', address, name='address')
]
