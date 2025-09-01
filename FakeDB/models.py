from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=25)
    employee_age = models.IntegerField()
    employee_email = models.EmailField()
    employee_salary = models.IntegerField()
    employee_address = models.CharField(max_length=35)

    def __str__(self):
        return self.employee_name


