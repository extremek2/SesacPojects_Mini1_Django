from django.db import models

class Seller(models.Model):
    username = models.CharField(max_length=10, unique=True)
    sellerName = models.CharField(max_length=10)
    password = models.CharField(max_length=10)  # 평문 저장
    store_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username