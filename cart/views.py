import item
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import CartItem
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order,OrderItem
# Create your views here.
def cart(request):
    return render(request, 'cart/detail.html')
@login_required
def detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    return render(request, 'cart/cart_home.html', {
        'cart_items': cart_items,
        'total': total
    })
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_home')

@csrf_exempt
@login_required


def order_complete(request):
    items_list=[]
    if request.method == 'POST':
        items_raw = request.POST.get('items')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        try:
            parsed_items = json.loads(items_raw)
            items_list=parsed_items
        except:
            items_list=[]
            #parsed_items = []

        order=Order.objects.create(
            user=request.user,
            address=address,
            payment_method=payment_method,
        )

        for item in items_list:

            name,qty_part=item.split('(')
            quantity=int(qty_part.replace('개)',''))

            OrderItem.objects.create(
                order=order,
                product_name=name.strip(),
                quantity=quantity,
            )



        # 저장하고 다음 요청에서도 쓸 수 있도록 세션에 저장
        request.session['ordered_items'] = items_list

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




