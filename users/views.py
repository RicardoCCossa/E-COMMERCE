from django.contrib.auth import login as auth_login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import CustomerProfileForm, CustomerRegistrationForm, LoginForm
from users.models import Customer

# ================================
# Registro de cliente
# ================================
def custom_registration_view(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parabéns! Sua conta foi criada com sucesso.")
            return redirect("login")  # Redireciona para login após cadastro
        else:
            messages.error(request, "Ocorreu um erro ao criar sua conta. Verifique os campos.")
    else:
        form = CustomerRegistrationForm()

    return render(request, "users/customRegistration.html", {"form": form})


def custom_login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")  # Redireciona para home
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})

def custom_password_reset_view(request):
    return render(request, 'users/passwordReset.html')

@login_required
def profile(request):
    """
    View para criar ou atualizar o perfil do usuário logado.
    """
    # Obtém ou cria o perfil do utilizador autenticado
    customer, created = Customer.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Passa a instância existente para atualizar em vez de criar sempre
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil salvo com sucesso!')
            return redirect('profile')  # evita reenvio do formulário no refresh
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, 'users/profile.html', {'form': form})

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'users/address.html', {'add': add})

@login_required
def updateAddress(request, pk):
    """
    Permite ao usuário autenticado atualizar um endereço específico.
    """
    # Busca o endereço do próprio usuário. Se não existir, 404
    address = get_object_or_404(Customer, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Endereço atualizado com sucesso!')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomerProfileForm(instance=address)

    return render(request, 'users/updateAddress.html', {'form': form})
