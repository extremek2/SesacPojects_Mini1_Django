import item
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def cart(request):
    return render(request, 'cart/detail.html')
@login_required
def detail(request):
    user=request.user
    cart_items=CartItem.objects.filter(user=user)
    total=sum(item.total_price() for item in cart_items)
    return render(request, 'cart/detail.html', {'cart_items':cart_items, 'total':total})

@csrf_exempt
@login_required
def order_complete(request):
    if request.method == 'POST':
        items=request.POST.get('items')
        try:
            parsed_items = json.loads(items)
        except:
            parsed_items = []

        # 저장하고 다음 요청에서도 쓸 수 있도록 세션에 저장
        request.session['ordered_items'] = parsed_items

        return redirect('order_complete')

        # GET 요청 시 세션에서 꺼냄
    items = request.session.get('ordered_items', [])
    return render(request, 'cart/order_complete.html', {
        'items': items
    })



#그이전 코딩
   ##items=request.session.get('orderded_items',[])
    ##return render(request,'cart/order_complete.html',{'items':items})
#


    ##cart_items=[

      ##  {'name':'양배추', 'price':1000, 'quantity':1,
        ## 'image':"../../static/assets/img/greenball.jpg"},

      ##  {'name':'감자', 'price':2000,  'quantity':1,
       ##  'image':"../../static/assets/img/potato.jpg"},

     ##  'image':"../../static/assets/img/tomato.jpg"},



   ##]

    ##total=sum(item['price'] * item['quantity'] for item in cart_items)

    ##return render(request, 'cart/detail.html', {'total':total})

