from django.urls import path
from meteoro import views
from django.views.generic import TemplateView


urlpatterns = [
    # ================================
    # Páginas principais
    # ================================
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ================================
    # Produtos e categorias
    # ================================
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('category-title/<slug:title_slug>/', views.category_title, name='category_title'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'), 

    # ================================
    # Carrinho e checkout
    # ================================
    path('cart/', views.show_cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='cart_add'),
    path('checkout/', views.checkout, name='checkout'),
    path('pedido-confirmado/', TemplateView.as_view(template_name="meteoro/order_confirmed.html"), name='order_confirmed'),

    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),


]
