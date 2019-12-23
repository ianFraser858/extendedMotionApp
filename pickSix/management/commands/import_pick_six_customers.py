from django.core.management import BaseCommand
from customers.models import Customer
import csv


# The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename')

    # A command must define handle()
    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename, newline='') as csvfile:
            # skips the first row which is column names
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                ship_to_account_number, \
                    corp, \
                    territory, \
                    territory_description, \
                    group, \
                    division, \
                    mi_loc, \
                    location_description, \
                    customer_no, \
                    customer_name = row[:]

                customer, created = Customer.objects.get_or_create(ship_to_account_number=ship_to_account_number)

                customer.corp = corp
                customer.territory = territory
                customer.territory_description = territory_description
                customer.group = group
                customer.division = division
                customer.mi_loc = mi_loc
                customer.location_description = location_description
                customer.customer_no = customer_no
                customer.customer_name = customer_name
                customer.save()
