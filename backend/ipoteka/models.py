from pyexpat import model
from django.db import models


class MortgageOffers(models.Model):
    bank_name = models.CharField(max_length=100)
    mortgage_rate = models.FloatField(default=0)
    mortgage_payment = models.IntegerField(default=0)

    def __str__(self):
        return self.bank_name