from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
##새로만든 부분
    path('cart/', views.cart_view, name='cart'),
    path('cart/update/', views.update_cart_api, name='cart_update'),  # 옵션: AJAX용

]

from django.urls import path, include

urlpatterns = [
    path('', include('single_pages.urls')),  # 필요에 따라 접두어 변경
    # other patterns...
]