from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from .Forms import EmployeeRegisterForm
from .models import Employees

def getempdetails(request):
    emp = Employees.objects.all()
    return render(request,"FakeDB/EmpDetails.html", context={"emp":emp})

def addempdetails(request):
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee data succesffuly added into the database")

    else:
        form = EmployeeRegisterForm()
        return render(request,"FakeDB/AddEmp.html", context={"form": form})

def deleteempdetails(request,id):
    emp = Employees.objects.get(employee_id=id)
    emp.delete()
    return HttpResponse("The employee data successfully deleted from the database")


def updateempdetails(request,id):
    emp = Employees.objects.get(employee_id=id)
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee data succesffuly updated")
    else:
        return render(request,"FakeDB/UpdateEmp.html",context={"emp":emp})
def sample:
    print("hello")