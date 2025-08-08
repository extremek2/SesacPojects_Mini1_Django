from django.shortcuts import render


def index(request):
    return render(request, 'single_pages/index.html')

def starter(request):
    return render(request, 'single_pages/starter-page.html')
# Create your views here.
