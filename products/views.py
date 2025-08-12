from django.shortcuts import render
from .models import SeasonalProducts, Products, Category

def products_index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    seasonal_products = SeasonalProducts.objects.all()
    return render(request, 'products/foody2_product.html',
                  context={'products': products,
                           'seasonal_products': seasonal_products,
                           'categories': categories})

def category(request, slug):
    categories = Category.objects.all()
    # for category in categories:

    if slug == "no_category":
        products = Products.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        products = Products.objects.filter(category=category)
    return render(request,
                  template_name='products/foody2_product.html',
                  context={'products': products, 'categories': categories})


def detail(request, pk):
    product = Products.objects.get(pk=pk)
    categories = Category.objects.all()

    return render(request,
                  template_name='products/product_detail.html',
                  context={'product': product,
                           'categories': categories})


