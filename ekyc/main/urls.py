from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify_phone, name='verifyphone'),
    path('verifyids/', views.verify_ids, name='verifyids'),
    path('verifyotp/', views.verify_otp, name='verifyotp'),
    path('verifydocs/', views.verify_docs, name='verifydocs'),
    path('video/', views.video, name='video'),
    path('video/upload', views.video),
    path('deleteotp/', views.delete_otp, name='deleteotp'),
]    
