from django.db import models


class MortgageOffers(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment = models.IntegerField(default=0) # Платеж в месяц
    bank_name = models.CharField(max_length=100)
    term_min = models.IntegerField(default=0)  # Срок ипотеки, ОТ
    term_max = models.IntegerField(default=0)  # Срок ипотеки, ДО
    rate_min = models.FloatField(default=0)  # Ставка, ОТ
    rate_max = models.FloatField(default=0)  # Ставка, ДО
    payment_min = models.IntegerField(default=0)  # Сумма кредита, ОТ
    payment_max = models.IntegerField(default=0)  # Сумма кредита, ДО

    def __str__(self):
        return self.bank_name
