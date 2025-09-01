import os
from random import randint
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","Facebook.settings")
django.setup()


from FakeDB.models import Employees
from faker import Faker

faker = Faker()

def getemployeesdata():
    f_empId = randint(200,999)
    f_empName = faker.name()
    f_empAge = randint(1,99)
    f_empEmail = faker.email()
    f_empSalary = randint(30000,60000)
    f_empAddress = faker.city()

    emp = Employees.objects.get_or_create(employee_id=f_empId,
employee_name = f_empName, employee_age=f_empAge, employee_email = f_empEmail, employee_salary=f_empSalary, employee_address=f_empAddress)

for i in range(10):
    getemployeesdata()
