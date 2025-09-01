from django.contrib import admin
from django.urls import path, include
#  localhost:8038/Four/
from . import views

urlpatterns = [
    path('getdata/',views.getempdetails),
    path('deletedata/<id>', views.deleteempdetails),
    path('addemp/', views.addempdetails),
    path('updatedata/<id>',views.updateempdetails)
]