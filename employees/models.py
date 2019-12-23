from django.db import models
from datetime import date


# Create your models here.


class Employee(models.Model):

    employee_id = models.CharField(max_length=6, primary_key=True)
    mi_account = models.CharField(max_length=8)
    employee_mi_loc = models.CharField(max_length=4)
    employee_name = models.CharField(max_length=100)
    employee_title = models.CharField(max_length=40, null=True, blank=True)
    employee_dept = models.CharField(max_length=25, null=True, blank=True)
    job_code = models.CharField(max_length=5)
    job_status = models.CharField(max_length=5, null=True, blank=True)
    job_position = models.CharField(max_length=30, null=True, blank=True)
    supervisor_id = models.CharField(max_length=6, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_updated_date = models.DateField(default=date.today, editable=False)

    class Meta:
        ordering = ['employee_mi_loc']

    @property
    def name(self):
        return u'{} {}'.format(self.employee_id, self.mi_account)

    def __str__(self):
        return self.employee_id
