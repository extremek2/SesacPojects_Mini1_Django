from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse





def index(request):
    return render(request, 'single_pages/index.html')

def starter(request):
    return render(request, 'single_pages/starter-page.html')




##새로 만든 json부분
from django.http import JsonResponse
import json
def cart_view(request):
    # session에 'cart'가 있으면 사용, 없으면 샘플 데이터로 초기화 (개발용)
    cart = request.session.get('cart')
    if cart is None:
        cart = [
            {'id': 1, 'name': '국산 무', 'price': 3000, 'quantity': 2},
            {'id': 2, 'name': '신선한 배추', 'price': 5000, 'quantity': 1},
            {'id': 3, 'name': '달콤한 당근', 'price': 2500, 'quantity': 3},
        ]
        request.session['cart'] = cart

    total = sum(item['price'] * item['quantity'] for item in cart)
    # cart_items_json은 템플릿의 JS에서 사용하기 위함 (한글 깨짐 방지)
    return render(request, 'single_pages/cart.html', {
        'cart_items': cart,
        'total': total,
        'cart_items_json': json.dumps(cart, ensure_ascii=False)
    })
    # (옵션) 수량 변경 / 삭제를 위한 API 엔드포인트 예시
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@require_POST
def update_cart_api(request):
    data = json.loads(request.body.decode('utf-8'))
    item_id = int(data.get('id'))
    quantity = int(data.get('quantity', 1))

    cart = request.session.get('cart', [])
    for it in cart:
        if it['id'] == item_id:
            it['quantity'] = max(1, quantity)
            break
    request.session['cart'] = cart
    total = sum(i['price']*i['quantity'] for i in cart)
    return JsonResponse({'ok': True, 'cart': cart, 'total': total})