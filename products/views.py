from django.http import HttpResponseForbidden
from django.shortcuts import render
from seller.models import Seller
from .models import Products, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def products_index(request):
    # 현재 로그인한 사용자가 판매자인지 확인
    is_seller = Seller.objects.filter(user=request.user).exists()
    if is_seller:
        return HttpResponseForbidden("판매자님으로 로그인 되어있습니다. 고객님으로 로그인하시고 이용해주세요")

    products = Products.objects.all()
    categories = Category.objects.all()

    return render(request, 'products/foody2_product.html',
                  context={
                      'products': products,
                      'categories': categories
                  })


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


