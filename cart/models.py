from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(default=1)
    image_url=models.URLField(blank=True)

    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f'{self.user.username} - {self.product_name}'
# Create your models here.
