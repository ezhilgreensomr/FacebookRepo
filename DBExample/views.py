from django.shortcuts import render

from .models import Employees

def get_employees(request):

    emp_details = Employees.objects.all()

    emp = {"emp_details": emp_details}

    return render(request, "DBExample/Table.html",context=emp)
