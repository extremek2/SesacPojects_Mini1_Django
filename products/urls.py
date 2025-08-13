from django.urls import path
from . import views


urlpatterns = [

    path('',views.products_index,name='products_index'),
    path('<int:pk>/',views.detail,name='products_detail'),
    path('category/<slug>/', views.category, name='category'),
    path('cart/create/', views.create_cart, name='create_cart'),
]

