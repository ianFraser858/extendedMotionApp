from django.contrib import admin
from employees.models import Employee
from django_admin_listfilter_dropdown.filters import DropdownFilter


class EmployeeAdmin(admin.ModelAdmin):
    ordering = ['employee_mi_loc']
    list_filter = (('mi_account', DropdownFilter),
                   ('employee_mi_loc', DropdownFilter),
                   ('employee_dept', DropdownFilter),
                   ('job_code', DropdownFilter),
                   ('supervisor_id', DropdownFilter))
    list_display = ('employee_id', 'mi_account', 'employee_mi_loc', 'employee_name', 'employee_dept', 'job_code', 'supervisor_id')
    search_fields = ['mi_account', 'employee_mi_loc', 'employee_name', 'employee_dept', 'job_code', 'supervisor_id']


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
