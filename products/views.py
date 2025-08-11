from django.shortcuts import render
from .models import SeasonalProducts, Products

def products_index(request):
    products = Products.objects.all()
    seasonal_products = SeasonalProducts.objects.all()
    return render(request, 'products/index.html',
                  context={'products': products,
                           'seasonal_products': seasonal_products})

def detail(request, pk):
    product = Products.objects.get(pk=pk)

    return render(request,
                  template_name='products/product_detail.html',
                  context={'product': product})