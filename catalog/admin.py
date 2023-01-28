from django.contrib import admin

from .models import City, Client, Product, Retailer

admin.site.register(Retailer)
admin.site.register(City)
admin.site.register(Client)
admin.site.register(Product)
