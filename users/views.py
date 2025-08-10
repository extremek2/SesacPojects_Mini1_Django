from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#회원가입
def signup_(request,messages=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            from django.contrib import messages
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Successfully created user')
        return redirect('login')

    return render(request,'users/signup.html')

#로그인
def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'users/login.html')

#로그아웃
def logout_(request):
    logout(request)
    return redirect('index')