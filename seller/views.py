from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .forms import ProductForm
from .models import Seller
from django.views.decorators.http import require_POST

# 판매자 로그인
def seller_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                seller = Seller.objects.get(user=user)
                login(request, user)
                return redirect('seller_dashboard')
            except Seller.DoesNotExist:
                messages.error(request, '판매자 계정이 아닙니다')
        else:
            messages.error(request, '아이디 또는 비밀번호가 틀렸습니다')

    return render(request, 'seller/seller_login.html')

# 판매자 회원가입
def seller_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        sellerName = request.POST.get('sellerName')
        store_name = request.POST.get('store_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if password != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다')
            return redirect('seller_signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 아이디입니다')
            return redirect('seller_signup')

        user = User.objects.create_user(username=username, password=password)
        Seller.objects.create(
            user=user,
            sellerName=sellerName,
            store_name=store_name,
            phone_number=phone_number,
            address=address
        )
        return redirect('seller_login')

    return render(request, 'seller/seller_signup.html')

# 판매자 대시보드
def seller_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('seller_login')

    try:
        seller = Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        return redirect('seller_login')

    products = Products.objects.filter(seller=seller)

    return render(request, 'seller/dashboard.html', {
        'seller': seller,
        'products': products
    })

# 판매자 로그아웃
def seller_logout(request):
    logout(request)
    return redirect('seller_login')

# 판매자 상품 업로드
def seller_upload(request):
    if not request.user.is_authenticated:
        return redirect('seller_login')

    seller = get_object_or_404(Seller, user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = seller  # 로그인된 판매자 연결
            product.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm()

    return render(request, 'seller/seller_upload.html', {'form': form})

