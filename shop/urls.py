# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 여기에 상품 관련 URL을 나중에 넣으면 됨
     path('', views.product_list, name='product_list'),
]