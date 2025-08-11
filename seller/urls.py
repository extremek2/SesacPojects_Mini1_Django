from django.urls import path
from . import views


urlpatterns = [
    path('',views.seller_login,name='seller_login'),


]
