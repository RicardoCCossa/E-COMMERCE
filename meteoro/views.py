from django.shortcuts import redirect, render, get_object_or_404

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

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user = user, product = product).save()
    return redirect('cart/')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user = user)
    return render(request, 'meteoro/addtocart.html')


