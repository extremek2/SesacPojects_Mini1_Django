from seller.models import Seller

def is_seller_context(request):
    is_seller = False
    if request.user.is_authenticated:
        is_seller = Seller.objects.filter(user=request.user).exists()
    return {'is_seller': is_seller}
