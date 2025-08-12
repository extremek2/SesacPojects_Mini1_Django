from django.urls import path
from . import views

urlpatterns = [
    path('seller_signup/',views.seller_signup,name='seller_signup'),
    path('seller_login/',views.seller_login,name='seller_login'),
    path('seller_logout/', views.seller_logout, name='seller_logout'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller_upload/', views.seller_upload, name='seller_upload'),
    # path('seller/product/edit/<int:product_id>/', views.edit_product, name='seller_product_edit'),
    # path('seller/product/delete/<int:product_id>/', views.delete_product, name='seller_product_delete'),

]

