from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product_name=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name}x {self.quantity}"


##더미데이터
class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

##class CartItem(models.Model):
 ##   user=models.ForeignKey(User,on_delete=models.CASCADE)
 ##   product_name=models.CharField(max_length=100)
 ##   price=models.PositiveIntegerField()
 ##   quantity=models.PositiveIntegerField(default=1)
  ##  image_url=models.URLField(blank=True)

  ##  def total_price(self):
  ##      return self.price * self.quantity
  ##  def __str__(self):
   ##     return f'{self.user.username} - {self.product_name}'


# Create your models here.
