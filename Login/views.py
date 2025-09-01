from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"FirstWebApp/Home.html")

def login(request):
    return render(request,"FirstWebApp/Login.html")

def signup(request):
    return render(request,"FirstWebApp/SignUp.html")