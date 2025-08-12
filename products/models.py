from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from seller.models import Seller
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    itemcode = models.IntegerField(unique=True)
    itemname = models.CharField(max_length=20)
    itemcategorycode = models.IntegerField()
    itemcategoryname = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100,
                            unique=True,
                            allow_unicode=True)
    def __str__(self):
        return f'{self.itemname}'
    def get_category_url(self):
        return f'/products/category/{self.slug}'

class Products(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    uploaded_image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return f'-이름:{self.name} - 가격{self.price} - 수량{self.quantity} 판매자ID[{self.seller}]'
                #  - 판매자{self.seller}
    def get_absolute_url(self):
        return f'/products/{self.pk}/'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} - {self.address} - {self.paymentmethod} - {self.created_at}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'{self.quantity} x {self.product.name} in Order {self.order.id}'


class SeasonalProducts(models.Model):
    # 식품번호
    idntfc_no = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 품목명(기장 등)
    prdlst_nm = models.CharField(max_length=20)
    # 월별(9월)
    m_distctns = models.CharField(max_length=20)
    # 월별농식품
    m_distctns_itm = models.CharField(max_length=20)
    # 품목분류
    prdlst_cl = models.CharField(max_length=20)
    # 주요 산지
    mtc_nm = models.CharField(max_length=100)
    # 생산시기
    prdctn_era = models.CharField(max_length=20)
    # 주요 품종
    main_spcies_nm = models.CharField(max_length=20, null=True)
    # 효능
    effect = models.CharField(max_length=300)
    # 구입요령
    purchase_mth = models.CharField(max_length=300)
    # 조리법
    cook_mth = models.CharField(max_length=300)
    # 손질요령
    trt_mth = models.CharField(max_length=300)
    # 상세페이지 URL
    url = models.CharField(max_length=100)
    # 이미지 URL
    img_url = models.CharField(max_length=100)
    # 등록일
    regist_de = models.DateTimeField()

    def __str__(self):
        return f'{self.idntfc_no}-{self.prdlst_nm}-{self.m_distctns}-{self.m_distctns_itm}-{self.prdlst_cl}-{self.mtc_nm}-{self.prdctn_era}-{self.main_spcies_nm}-{self.effect}-{self.purchase_mth}-{self.cook_mth}-{self.trt_mth}-{self.url}-{self.img_url}-{self.regist_de}'