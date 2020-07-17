from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('login/', views.login, name='user_login'),
    # path('logout/', views.logout, name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('register_success/', views.register_success, name='user_register_success'),
    path('login', views.login, name='api_login'),
    path('upload_data', views.upload_data, name='api_upload_data'),
]
