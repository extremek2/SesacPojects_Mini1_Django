from django.urls import path
from . import views

urlpatterns = [

    path('',views.detail,name='cart'),
    path('order-complete/',views.order_complete,name='order_complete'),
    path('delete/<int:item_id>/', views.cart_delete, name='cart_delete'),
]