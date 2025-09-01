from django.shortcuts import render

from . import Form

# Create your views here.
from .models import RegisterModel


def Register(request):

    if(request.method == "POST"):
        if (request.POST.get("username") and request.POST.get("password") and request.POST.get("confirm_password") and
                request.POST.get("email") and request.POST.get("phoneNo") and request.POST.get(
                    "address") and request.POST.get("age")):
            reg = RegisterModel()
            reg.username = request.POST.get("username")
            reg.password = request.POST.get("password")
            reg.confirm_password = request.POST.get("confirm_password")
            reg.email = request.POST.get("email")
            reg.phoneNo = request.POST.get("phoneNo")
            reg.address = request.POST.get("address")
            reg.age = request.POST.get("age")
            reg.save()

    #objectname = classname()
    register = Form.RegisterForm()
    # reg = {"Register": register}
    return render(request,"FormApp/Register.html", context={"Register": register})