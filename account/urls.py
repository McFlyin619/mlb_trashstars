from django.contrib import admin
from django.urls import path, include
from .views import register

app_name = 'account_app'
urlpatterns = [
    path('register/',register, name='register'),
]
