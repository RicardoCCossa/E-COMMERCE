from django.urls import path
from meteoro.views import (
    add_to_cart,
    index,
    about,
    contact,
    category,
    category_title,
    product_detail,
    show_cart,
    
)

urlpatterns = [
    # ================================
    # Páginas principais
    # ================================
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
    # ================================
    # Produtos e categorias
    # ================================
    path('category/<category_slug>/', category, name='category'),
    path('category-title/<title_slug>/', category_title, name='category_title'),
    path('product/<int:pk>/', product_detail, name='product_detail'), 

    # Add to cart
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', show_cart, name='show_cart')
]
