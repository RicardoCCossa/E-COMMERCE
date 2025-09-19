from django.contrib import admin
from .models import Product

class Products(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image')
    list_display_links = ('id', 'title',)

admin.site.register(Product, Products)