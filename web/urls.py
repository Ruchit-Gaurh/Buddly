from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('home', views.home),
    path('register_page', views.register_page, name='register_page'),
    path('register', views.register, name='register'),
    path('login_page', views.login_page, name='login_page'),
    path('login', views.loginn, name='login'),
    path('chat', views.chat, name='chat'),
]
