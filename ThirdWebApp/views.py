from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contactpage(request):
    return HttpResponse("Contact Details")
