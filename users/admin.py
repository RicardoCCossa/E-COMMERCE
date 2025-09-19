from django.contrib import admin
from users.models import Customer

class CustomerModel(admin.ModelAdmin):
    list_display = ('user', 'name', 'locality', 'city', 'mobile', 'zipcode', 'state')
    list_display_links = ('user', 'name',)

admin.site.register(Customer, CustomerModel)