from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from single_pages.models import Product


# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 로그인한 사용자의 장바주니 가져오기(없으면 만들기)


    item, created = Cart.objects.get_or_create(user=request.user)
    item,created =Cart.objects.get_or_create(cart=cart,product=product)
    if not created:
        item.quantity += 1
        item.save()

        return redirect('/cart')


def cart_detal(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.cart_items_set.all()
    return render(request,'cart/cart.html',{'items':items})