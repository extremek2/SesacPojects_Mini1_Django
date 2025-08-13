from django.urls import path
from . import views


urlpatterns = [
    path('',views.products_index,name='products_index'),


]
