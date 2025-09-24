from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from django.contrib.auth.models import User

from users.models import Customer


# Login
class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Nome de usuário',
            'id': 'floatingUsername'
        })
    )
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control',
            'placeholder': 'Senha',
            'id': 'floatingPassword'
        })
    )


# Cadastro de usuário
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário',
            'id': 'floatingUsername'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'id': 'floatingEmail'
        })
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha',
            'id': 'floatingPassword1'
        })
    )
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme a senha',
            'id': 'floatingPassword2'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Alterar senha autenticado
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha atual",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'autocomplete': 'current-password',
            'class': 'form-control',
            'placeholder': 'Digite sua senha atual',
            'id': 'floatingOldPassword'
        })
    )
    new_password1 = forms.CharField(
        label="Nova senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'placeholder': 'Digite a nova senha',
            'id': 'floatingNewPassword1'
        })
    )
    new_password2 = forms.CharField(
        label="Confirme a nova senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'placeholder': 'Confirme a nova senha',
            'id': 'floatingNewPassword2'
        })
    )


# Recuperar senha (envio de email)
class MyPasswordResetForm(PasswordResetForm):
    # Coloque o texto que quer ver flutuando no label (aqui deixei a mensagem completa)
    email = forms.EmailField(
        label='Digite seu e-mail cadastrado',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autofocus': 'autofocus',
            'class': 'form-control',
            # Para form-floating o placeholder precisa existir — pode ser um espaço
            'placeholder': ' ',
            'id': 'floatingEmail',
            'autocomplete': 'email',
        })
    )


# Definir nova senha (via link)
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a nova senha'
        })
    )
    new_password2 = forms.CharField(
        label='Confirme a nova senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme a nova senha'
        })
    )


# Perfil / Endereço do cliente
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']

        labels = {
            'name': 'Nome completo',
            'locality': 'Bairro / Localidade',
            'city': 'Cidade',
            'mobile': 'Telefone / Telemóvel',
            'state': 'Província / Estado',
            'zipcode': 'Código Postal',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo',
                'id': 'floatingName'
            }),
            'locality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o bairro ou localidade',
                'id': 'floatingLocality'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a cidade',
                'id': 'floatingCity'
            }),
            'mobile': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o telefone',
                'id': 'floatingMobile'
            }),
            'state': forms.Select(attrs={
                'class': 'form-control',
                'id': 'floatingState'
            }),
            'zipcode': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o código postal',
                'id': 'floatingZipcode'
            }),
        }
