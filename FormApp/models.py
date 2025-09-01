from django.db import models

# Create your models here.


class RegisterModel(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNo = models.IntegerField()
    address = models.CharField(max_length=25)
    age = models.IntegerField()
