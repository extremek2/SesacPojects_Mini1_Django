from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from seller.models import Seller


# Create your views here.
#회원가입
def signup_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'users/signup.html')

#로그인
def login_(request):
    # 판매자로 로그인된 상태라면 로그아웃 + 메시지
    if request.user.is_authenticated:
        if Seller.objects.filter(user=request.user).exists():
            logout(request)
            messages.info(request, '기존 판매자 계정에서 로그아웃되었습니다.')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, '아이디 또는 비밀번호가 틀렸습니다')

    return render(request, 'users/login.html')


#로그아웃
def logout_(request):
    logout(request)
    return redirect('index')