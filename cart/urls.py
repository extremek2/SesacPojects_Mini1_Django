from django.urls import path
from . import views

urlpatterns = [

    path('',views.cart,name='cart'),
    path('order-complete/',views.order_complete,name='order_complete'),
]