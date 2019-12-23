from django.db import models
from employees.models import Employee
from customers.models import Customer

# Create your models here.


class PickSixSelection(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    # def __str__(self):
    #     return '1'
