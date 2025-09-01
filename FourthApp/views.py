from django.shortcuts import render

# Create your views here.
# localhost:8058/Four/login
def login(request):
    return render(request,"FourthWebApp/SampleForm.html")

def home(request):
    laptop = int(request.GET['laptop'])
    tablet = int(request.GET["tablet"])
    mobile = int(request.GET["mobile"])
    tv = int(request.GET["tv"])

    total_price = laptop+tablet+mobile+tv

    price = {"total": total_price}

    return render(request, "FourthWebApp/HomePage.html", price)