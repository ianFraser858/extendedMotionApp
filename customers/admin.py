from django.contrib import admin
from customers.models import Customer
from django_admin_listfilter_dropdown.filters import DropdownFilter


# sorts the guests by last name in the admin interface
class CustomerAdmin(admin.ModelAdmin):
    ordering = ['ship_to_account_number']
    list_filter = (('mi_loc', DropdownFilter),
                   ('customer_no', DropdownFilter),
                   ('customer_name', DropdownFilter))
    list_display = ('ship_to_account_number', 'mi_loc', 'customer_no', 'customer_name')
    search_fields = ['ship_to_account_number', 'mi_loc', 'customer_no', 'customer_name']


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
