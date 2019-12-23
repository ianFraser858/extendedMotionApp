from django import forms
from django.core.exceptions import ValidationError
from django_select2.forms import Select2MultipleWidget
from customers.models import Customer


class PickSixForm(forms.Form):
    def check_length(self):
        if len(self) > 6:
            raise ValidationError('too many')

    employee = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Employee Number',
                                                                       'style': 'width:85%',
                                                                       'style': 'align:center'}))
    customers = forms.ModelMultipleChoiceField(queryset=Customer.objects.all(), widget=Select2MultipleWidget(), label='', validators=[check_length])


