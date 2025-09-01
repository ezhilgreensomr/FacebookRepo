from django.contrib import admin
from django.urls import path, include
#  localhost:8038/Four/

from . import views

urlpatterns = [
    # http:localhost:8080/DBExample/getemployees
    path('getemployees/', views.get_employees),
]

