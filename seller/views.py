from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .forms import ProductForm,SellerForm
from .models import Seller
from django.views.decorators.http import require_POST

# 판매자 로그인

def seller_login(request):
    #이미 로그인된 사용자가 있으면 로그아웃
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, '기존 고객 계정에서 로그아웃되었습니다.')

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

#상품수정함수
def update_product(request, product_id):
    # 로그인 여부 확인
    if not request.user.is_authenticated:
        messages.warning(request, '로그인이 필요합니다.')
        return redirect('seller_login')

    # 로그인한 판매자 정보 가져오기
    seller = get_object_or_404(Seller, user=request.user)

    # 해당 판매자의 상품인지 확인
    product = get_object_or_404(Products, id=product_id, seller=seller)

    # POST 요청일 경우: 수정 처리
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, '상품이 성공적으로 수정되었습니다.')
            return redirect('seller_dashboard')
        else:
            messages.error(request, '입력한 정보에 오류가 있습니다. 다시 확인해주세요.')
    else:
        # GET 요청일 경우: 기존 정보로 폼 생성
        form = ProductForm(instance=product)

    # 템플릿에 기존 상품 정보와 수정 폼 전달
    return render(request, 'seller/update_product.html', {
        'form': form,
        'product': product
    })


#상품삭제
@require_POST
def delete_product(request, product_id):
    if not request.user.is_authenticated:
        return redirect('seller_login')

    seller = get_object_or_404(Seller, user=request.user)
    product = get_object_or_404(Products, id=product_id, seller=seller)

    product.delete()
    messages.success(request, '상품이 삭제되었습니다.')
    return redirect('seller_dashboard')


#판매자 정보수정
def seller_update(request):
    seller = Seller.objects.get(user=request.user)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'seller/seller_update.html', {'form': form})
