from pyexpat import model
from django.db import models


class MortgageOffers(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100)
    term_min = models.IntegerField(default=0)
    term_max = models.IntegerField(default=0)
    rate_min = models.FloatField(default=0)
    rate_max = models.FloatField(default=0)
    payment_min = models.IntegerField(default=0)
    payment_max = models.IntegerField(default=0)

    def __str__(self):
        return self.bank_name