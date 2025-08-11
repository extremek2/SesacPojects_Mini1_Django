from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse





def index(request):
    return render(request, 'single_pages/index.html')

def starter(request):
    return render(request, 'single_pages/starter-page.html')




