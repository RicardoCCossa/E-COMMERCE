from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Product

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
    return render(request, "meteoro/addtocart.html", {"cart_items": cart_items})


# ================================
# Checkout
# ================================
def checkout(request):
    # Em breve: lógica para finalizar a compra
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "meteoro/checkout.html", {"cart_items": cart_items})
