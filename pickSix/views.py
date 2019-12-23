from django.shortcuts import render, redirect
from django.contrib import messages
from customers.models import Customer
from employees.models import Employee
from pickSix.models import PickSixSelection
from pickSix.forms import PickSixForm

# Create your views here.


def home(request):
    form = PickSixForm()
    context = {'form': form}
    return render(request, 'pickSix/home.html', context)


def pick_six_selection(request):
    if request.method == 'POST':
        try:
            form = PickSixForm(request.POST)
            if form.is_valid():
                customers = form.cleaned_data['customers']
                employee_id = form.cleaned_data['employee']
                does_employee_exist = Employee.objects.get(employee_id=employee_id)
                num_customers_assigned = PickSixSelection.objects.filter(employee_id=employee_id)

                if len(customers) + len(num_customers_assigned) > 6:
                    messages.error(request, ' You have selected too many customers! ')
                else:
                    for entry in customers:
                        PickSixSelection.objects.get_or_create(employee=does_employee_exist, customer=entry)
        except Employee.DoesNotExist:
            messages.error(request, ' Not a valid employee number ')

        return redirect('home')





