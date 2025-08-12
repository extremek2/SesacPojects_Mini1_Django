import item
from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'cart/detail.html')

def detail(request):
    cart_items=[

        {'name':'양배추', 'price':1000, 'quantity':1,
         'image':"../../static/assets/img/greenball.jpg"},

        {'name':'감자', 'price':2000,  'quantity':1,
         'image':"../../static/assets/img/potato.jpg"},

        {'name': '토마토', 'price': 3000, 'quantity': 1,
         'image':"../../static/assets/img/tomato.jpg"},



    ]

    total=sum(item['price'] * item['quantity'] for item in cart_items)

    return render(request, 'cart/detail.html', {'total':total})

