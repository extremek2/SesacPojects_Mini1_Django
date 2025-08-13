from django.urls import path
from . import views

urlpatterns = [

    path('',views.detail,name='cart'),
    path('order-complete/',views.order_complete,name='order_complete'),
]