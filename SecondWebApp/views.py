from django.shortcuts import render

from datetime import date

# Create your views here.
def student_datas(request):

    result = date.today()
    details = {"count":"5", "date": result, "place": "chennai"}
    return render(request,"SecondWebApp/StudentTable.html",details)

# render(request,html,context)