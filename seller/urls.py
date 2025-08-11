from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('seller_signup/',views.seller_signup,name='seller_signup'),
    path('seller_login/',views.seller_login,name='seller_login'),
    path('seller_logout/', views.seller_logout, name='seller_logout'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller_upload/', views.seller_upload, name='seller_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
