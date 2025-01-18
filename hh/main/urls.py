from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('log_in/', UserLoginView.as_view(), name='log_in'),
    path('log_out/', UserLogoutView.as_view(), name='log_out'),
    path('register/', register, name='register'),
    path('workers_list/', workers_list, name='workers_list'),
    path('create_user/', Create_User.as_view(), name='create_user')
]
