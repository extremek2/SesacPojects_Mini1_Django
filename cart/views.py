import item
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

# Create your views here.
def cart(request):
    return render(request, 'cart/detail.html')
@login_required
def detail(request):
    user=request.user
    cart_items=CartItem.objects.filter(user=user)
    total=sum(item.total_price() for item in cart_items)
    return render(request, 'cart/detail.html', {'cart_items':cart_items, 'total':total})
    ##cart_items=[

      ##  {'name':'양배추', 'price':1000, 'quantity':1,
        ## 'image':"../../static/assets/img/greenball.jpg"},

      ##  {'name':'감자', 'price':2000,  'quantity':1,
       ##  'image':"../../static/assets/img/potato.jpg"},

     ##  'image':"../../static/assets/img/tomato.jpg"},



   ##]

    ##total=sum(item['price'] * item['quantity'] for item in cart_items)

    ##return render(request, 'cart/detail.html', {'total':total})

