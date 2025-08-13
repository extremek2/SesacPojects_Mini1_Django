from django.urls import path
from . import views

urlpatterns = [

    path('',views.cart,name='cart'),
    path('order-complete/',views.order_complete,name='order_complete'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]