from django.contrib import admin

from products.models import Products, Category, CartItem

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(CartItem)

# Register your models here.
