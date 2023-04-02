from django.db import models

from django.db import models
# Create your models here.


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    date_of_joining = models.DateField()
    photo_file_name = models.CharField(max_length=500)

