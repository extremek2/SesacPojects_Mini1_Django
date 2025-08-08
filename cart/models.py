from django.db import models
from django.contrib.auth.models import User
from single_pages.models import Product  # 상품 모델이 있다고 가정

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 장바구니 주인

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)     # 어떤 장바구니에 속하는지
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # 어떤 상품인지
    quantity = models.PositiveIntegerField(default=1)             # 몇 개 담았는지