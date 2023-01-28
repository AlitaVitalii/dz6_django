from django.contrib import admin
from .models import Retailer, City, Client, Product

admin.site.register(Retailer)
admin.site.register(City)
admin.site.register(Client)
admin.site.register(Product)