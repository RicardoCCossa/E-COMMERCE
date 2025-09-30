from django.contrib import admin
from .models import Product, Cart

class Products(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image')
    list_display_links = ('id', 'title',)

admin.site.register(Product, Products)

class Carts(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    list_display_links = ('id', 'user',)

admin.site.register(Cart, Carts)