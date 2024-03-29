from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from chat.views import index
from account import views
from django import forms

urlpatterns = [
    path('', index),
    path('accounts/login/', LoginView.as_view()),
    path('accounts/logout/', LogoutView.as_view()),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
]
