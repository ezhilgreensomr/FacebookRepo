"""
URL configuration for Facebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#  localhost:8038/Four/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Login.urls")),
    path('second/', include("SecondWebApp.urls")),
    path('third/', include("ThirdWebApp.urls")),
    path('Four/', include("FourthApp.urls")),
    path('DBExample/', include("DBExample.urls")),
    path('form/', include("FormApp.urls")),
    path('fake/',include("FakeDB.urls")),
    path('alert/', include("AlertWebApp.urls")),
]


# http://localhost:8000/Four/login