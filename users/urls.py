from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('login/', views.login, name='user_login'),
    # path('logout/', views.logout, name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('register/success/', views.register_success, name='user_register_success'),
    path('login', views.login, name='api_login'),
    path('upload/tcn', views.upload_tcn, name='api_upload_tcn'),
    path('upload/tcn/rx', views.upload_tcn_rx, name='api_upload_tcn_rx'),
    path('upload/tcn/tx', views.upload_tcn_tx, name='api_upload_tcn_tx'),
    path('upload/attack/log', views.upload_attack_log, name='api_upload_attack_log'),
    path('update/exp_id', views.update_exp_id, name='api_update_exp_id')
]
