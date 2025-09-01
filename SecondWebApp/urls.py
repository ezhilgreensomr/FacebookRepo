from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('studentdatas/',views.student_datas)
]
