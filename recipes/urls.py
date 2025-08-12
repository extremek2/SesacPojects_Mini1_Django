from django.urls import path
from . import views


urlpatterns = [
    path('',views.recipes_index,name='recipes_index'),


]