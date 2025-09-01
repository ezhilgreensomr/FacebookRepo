from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def getdetails(request):
    print("View called")  # debug log
    return render(request, "AlertWebApp/Home.html")

def success_alert(request):
   messages.success(request,"Form Submitted Successfully")
   return render(request,"AlertWebApp/Home.html")

def error_alert(request):
   messages.error(request, "Something went wrong")
   return  render(request,"AlertWebApp/Home.html")

def warning_alert(request):
   messages.warning(request, "Are you sure want to delete")
   return  render(request,"AlertWebApp/Home.html")

def info_alert(request):
   messages.info(request, "This is just an info")
   return  render(request,"AlertWebApp/Home.html")