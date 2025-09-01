from django.contrib import admin
from django.urls import path, include
#  localhost:8038/form/register

from . import views

urlpatterns = [

    path('register/', views.Register),  # #//localhost:8080/form/register

]
