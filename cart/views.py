import item
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import CartItem,Order,OrderItem
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
# Create your views here.
def cart(request):
    return render(request, 'cart/detail.html')
@login_required
def detail(request):
    user=request.user
    cart_items=CartItem.objects.filter(user=user)
    total=sum(item.total_price() for item in cart_items)
    return render(request, 'cart/detail.html', {'cart_items':cart_items, 'total':total})

@require_POST
@login_required
def update_cart_quantity(request):
    user = request.user
    item_id = request.POST.get('item_id')
    quantity = request.POST.get('quantity')

    if not (item_id and quantity):
        return JsonResponse({'success': False, 'error': '잘못된 요청입니다.'})

    try:
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError
    except ValueError:
        return JsonResponse({'success': False, 'error': '수량은 1 이상의 정수여야 합니다.'})

    try:
        cart_item = CartItem.objects.get(id=item_id, user=user)
        cart_item.quantity = quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': '장바구니 아이템을 찾을 수 없습니다.'})

    return JsonResponse({'success': True, 'quantity': cart_item.quantity})

@login_required
def cart_delete(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        cart_item.delete()

    return redirect('cart')
@csrf_exempt
@login_required
def order_complete(request):
    if request.method == 'POST':
        items_raw = request.POST.get('items')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        try:
            items_list=json.loads(items_raw)

        except:
            items_list=[]


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
            #주문 완료 후 장바구니 비우기
            CartItem.objects.filter(user=request.user).delete()



        # 저장하고 다음 요청에서도 쓸 수 있도록 세션에 저장
        request.session['ordered_items'] = items_list
        request.session['order_info'] = {
            'order_id': order.id,
            'address': address,
            'payment_method': payment_method,
            'created_at': order.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # 포맷팅
            'total_price': sum(item.price * item.quantity for item in CartItem.objects.filter(user=request.user))
        }

        return redirect('order_complete')

        # GET 요청 시 세션에서 꺼냄
    items = request.session.get('ordered_items', [])
    order_info = request.session.get('order_info', {})
    return render(request, 'cart/order_complete.html', {
        'items': items,
    'order_info': order_info
    })



#그이전 코딩
   ##items=request.session.get('orderded_items',[])
    ##return render(request,'cart/order_complete.html',{'items':items})
#




