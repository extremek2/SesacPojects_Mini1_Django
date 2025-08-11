from django.urls import path
from . import views


urlpatterns = [
    path('',views.recipes_index,name='recipes_index'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail')

]
