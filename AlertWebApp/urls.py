from django.contrib import admin
from django.urls import path, include
#  localhost:8038/alert/sample
from . import views
urlpatterns = [
path('sample/', views.getdetails),
path('success/',views.success_alert),
path('error/',views.error_alert),
path('warning/',views.warning_alert),
path('info/',views.info_alert),
]