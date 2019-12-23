from django.db import models

# Create your models here.


class Customer(models.Model):

    ship_to_account_number = models.CharField(max_length=100, primary_key=True)
    corp = models.CharField(max_length=4)
    territory = models.CharField(max_length=6)
    territory_description = models.CharField(max_length=100)
    group = models.CharField(max_length=4)
    division = models.CharField(max_length=4)
    mi_loc = models.CharField(max_length=4)
    location_description = models.CharField(max_length=100)
    customer_no = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)

    class Meta:
        unique_together = (('customer_no', 'mi_loc'),)
        ordering = ['ship_to_account_number']

    @property
    def name(self):
        return u'{}'.format(self.account_name)

    def __str__(self):
        return self.ship_to_account_number
