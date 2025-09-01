from django.contrib import admin
from django.urls import path, include
#  localhost:8038/Four/

from . import views

urlpatterns = [
    path('login/', views.login),
    path('login/homepage', views.home)
]

# localhost:8080/Four/login
