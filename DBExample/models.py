from django.db import models

# Create your models here.
class Students(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=15)
    stu_address = models.CharField(max_length=25)
    stu_age = models.IntegerField()
    stu_mark = models.IntegerField()

    def __str__(self):
        return self.stu_name



class Employees(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=15)
    emp_age = models.IntegerField()
    emp_email = models.EmailField()
    emp_addr = models.CharField(max_length=30)

    def __str__(self):
        return self.emp_name







