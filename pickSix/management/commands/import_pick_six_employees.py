from django.core.management import BaseCommand
import ibm_db
from sqlalchemy import *

from employees.models import Employee
from utilities.db_driver import DbDriver


# The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):

        db2 = DbDriver()
        list_of_job_codes = ['4110', '4120', '4121', '4122', '4123', '4124']

        employee = Table(
            'EMPLOYEE', db2.metadata,
            Column('EMPLOYEE_ID', String),
            Column('MI_ACCOUNT', String),
            Column('EMP_MI_LOC', String),
            Column('EMP_NAME_CN', String),
            Column('EMP_TITLE', String),
            Column('EMP_DEPT', String),
            Column('JOB_CODE', String),
            Column('JOB_STATUS', String),
            Column('JOB_POSITION', String),
            Column('SUPERVISOR_ID', String)
        )
        s = employee.select().where(employee.c.JOB_CODE.in_(list_of_job_codes))
        result = db2.conn.execute('set schema EMPLOYEE')
        col_names = db2.conn.execute(s).keys()
        result = db2.conn.execute(s)

        for row in result:
            entry = dict(zip(col_names, row))
            employee, created = Employee.objects.get_or_create(employee_id=entry['EMPLOYEE_ID'])

            employee.mi_account = entry['MI_ACCOUNT'].strip()
            employee.employee_mi_loc = entry['EMP_MI_LOC'].strip()
            employee.employee_name = entry['EMP_NAME_CN'].strip()
            employee.employee_title = entry['EMP_TITLE'].strip()
            employee.employee_dept = entry['EMP_DEPT'].strip()
            employee.job_code = entry['JOB_CODE'].strip()
            employee.job_position = entry['JOB_STATUS'].strip()
            employee.job_status = entry['JOB_POSITION'].strip()
            employee.supervisor_id = entry['SUPERVISOR_ID'].strip()
            employee.save()



