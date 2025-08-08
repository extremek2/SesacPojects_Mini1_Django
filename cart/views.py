from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from single_pages.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 로그인한 사용자의 장바구니 가져오기 (없으면 만들기)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # 해당 상품이 장바구니에 있으면 수량 +1, 없으면 새로 추가
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/detail.html', {'cart': cart})