from django.contrib import admin

# Register your models here.
from .models import Students
from .models import Employees

admin.site.register(Students)
admin.site.register(Employees)