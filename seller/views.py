from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Products
from .forms import ProductForm
from .models import Seller


# Create your views here.
#판매자 로그인
def seller_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            seller = Seller.objects.get(username=username)
            if seller.password == password:
                request.session['seller_id'] = seller.id
                return redirect('seller_dashboard')
            else:
                messages.error(request, '비밀번호가 틀렸습니다')
        except Seller.DoesNotExist:
            messages.error(request, '존재하지 않는 판매자입니다')

    return render(request, 'seller/seller_login.html')

#판매자 회원가입
def seller_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        sellerName = request.POST.get('sellerName')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        store_name = request.POST.get('store_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if password != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다')
            return redirect('seller_signup')

        if Seller.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 판매자 아이디입니다')
            return redirect('seller_signup')

        Seller.objects.create(
            username=username,
            sellerName=sellerName,
            password=password,
            store_name=store_name,
            phone_number=phone_number,
            address=address
        )
        return redirect('seller_login')

    return render(request, 'seller/seller_signup.html')

# #판매자 상세페이지용
# def seller_dashboard(request):
#     seller_id = request.session.get('seller_id')
#     if not seller_id:
#         return redirect('seller_login')
#
#     seller = Seller.objects.get(id=seller_id)
#     return render(request, 'seller/dashboard.html', {'seller': seller})


def seller_dashboard(request):
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect('seller_login')

    seller = Seller.objects.get(id=seller_id)

    # 판매자가 등록한 상품들 조회
    products = Products.objects.filter(username=seller)

    return render(request, 'seller/dashboard.html', {
        'seller': seller,
        'products': products  # 상품 리스트도 템플릿에 전달
    })


#f판매자 로그아웃
def seller_logout(request):
    # 세션에서 seller_id 삭제
    if 'seller_id' in request.session:
        del request.session['seller_id']
    return redirect('seller_login')


def seller_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')  # 등록 후 이동할 페이지
    else:
        form = ProductForm()
    return render(request, 'seller/seller_upload.html', {'form': form})


