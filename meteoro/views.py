from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Product
from django.db.models import Q

# ================================
# Home Page
# ================================
def index(request):
    products = Product.objects.all()
    return render(request, "meteoro/index.html", {"products": products})


# ================================
# Páginas estáticas
# ================================
def about(request):
    return render(request, "meteoro/about.html")


def contact(request):
    return render(request, "meteoro/contact.html")


# ================================
# Produtos por categoria
# ================================
def category(request, category_slug):
    products = Product.objects.filter(category=category_slug)
    titles = products.values("title")
    return render(
        request,
        "meteoro/category.html",
        {
            "products": products,
            "titles": titles,
            "selected_category": category_slug,
        },
    )


# ================================
# Produtos com o mesmo título
# ================================
def category_title(request, title_slug):
    product = get_object_or_404(Product, title=title_slug)
    products = Product.objects.filter(category=product.category)
    titles = products.values("title")
    return render(
        request,
        "meteoro/category.html",
        {
            "products": products,
            "titles": titles,
            "selected_category": product.category,
        },
    )


# ================================
# Detalhes do produto
# ================================
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "meteoro/productdetail.html", {"product": product})


# ================================
# Carrinho de compras
# ================================
@login_required(login_url='login')
def add_to_cart(request):
    product_id = request.GET.get("prod_id")

    if not product_id:
        return redirect("cart")  # nenhum produto selecionado

    try:
        product_id = int(product_id)
    except ValueError:
        return redirect("cart")

    product = get_object_or_404(Product, id=product_id)

    # Se quiser evitar duplicados, podes usar get_or_create:
    Cart.objects.get_or_create(user=request.user, product=product)

    return redirect("cart")

def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    totalamount = sum(item.total_cost for item in cart_items)
    return render(request, "meteoro/addtocart.html", {
        "cart_items": cart_items,
        "totalamount": totalamount,
    })


# ================================
# Checkout
# ================================
from django.shortcuts import render, redirect
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    totalamount = sum(item.total_cost for item in cart_items)

    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        cidade = request.POST.get("cidade")
        bairro = request.POST.get("bairro")
        referencia = request.POST.get("referencia")

        if not all([nome, telefone, cidade, bairro]):
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
        else:
            # Aqui você poderia salvar as informações em um modelo Pedido (Order)
            messages.success(request, "✅ Pedido confirmado com sucesso! Entraremos em contacto para entrega.")
            # Limpa o carrinho (opcional)
            cart_items.delete()
            return redirect("home")  # ou outra página de sucesso

    return render(request, "meteoro/checkout.html", {
        "cart_items": cart_items,
        "totalamount": totalamount,
    })



from django.shortcuts import render, redirect
from .models import Cart, Order
from django.contrib import messages

def checkout(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    
    # Calcula total
    amount = sum(item.quantity * item.product.discounted_price for item in cart_items)
    totalamount = amount  # transporte grátis

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        province = request.POST.get("province")
        city = request.POST.get("city")
        neighborhood = request.POST.get("neighborhood")
        address = request.POST.get("address")

        # Cria o pedido
        order = Order.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            province=province,
            city=city,
            neighborhood=neighborhood,
            address=address,
            total=totalamount,
        )

        # Limpa o carrinho após confirmar
        cart_items.delete()

        messages.success(request, "✅ Pedido confirmado com sucesso!")
        return redirect("order_confirmed")

    context = {"cart_items": cart_items, "totalamount": totalamount}
    return render(request, "meteoro/checkout.html", context)




# ================================
# AJAX - Incrementar quantidade
# ================================
@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity += 1
            c.save()

            cart = Cart.objects.filter(user=request.user)
            amount = sum(p.quantity * p.product.discounted_price for p in cart)
            totalamount = amount  # transporte grátis

            data = {
                'quantity': c.quantity,
                'amount': f"{amount:.2f}",
                'totalamount': f"{totalamount:.2f}",
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado no carrinho'}, status=404)
    return JsonResponse({'error': 'Método inválido'}, status=400)


# ================================
# AJAX - Diminuir quantidade
# ================================
@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            if c.quantity > 1:
                c.quantity -= 1
                c.save()
            else:
                c.delete()

            cart = Cart.objects.filter(user=request.user)
            amount = sum(p.quantity * p.product.discounted_price for p in cart)
            totalamount = amount

            data = {
                'quantity': c.quantity if c.id else 0,
                'amount': f"{amount:.2f}",
                'totalamount': f"{totalamount:.2f}",
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    return JsonResponse({'error': 'Método inválido'}, status=400)


# ================================
# AJAX - Remover produto
# ================================
@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()

            cart = Cart.objects.filter(user=request.user)
            amount = sum(p.quantity * p.product.discounted_price for p in cart)
            totalamount = amount

            data = {
                'amount': f"{amount:.2f}",
                'totalamount': f"{totalamount:.2f}",
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    return JsonResponse({'error': 'Método inválido'}, status=400)

