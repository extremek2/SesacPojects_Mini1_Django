from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_,name='login'),
    path('signup/', views.signup_, name='signup'),
    path('logout/', views.logout_, name='logout'),

]
