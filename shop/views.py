# shop/views.py
from django.shortcuts import render
from .models import Product  # Product 모델 import

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})