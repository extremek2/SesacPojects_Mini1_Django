from django.shortcuts import render
from seller.views import Seller



def index(request, pk=None):
    is_seller = False
    if request.user.is_authenticated:
        is_seller = Seller.objects.filter(user=request.user).exists()

    context = {
        'pk': pk,
        'is_seller': is_seller,
    }

    return render(request, 'single_pages/index.html', context)


def starter(request):
    return render(request, 'single_pages/starter-page.html')



