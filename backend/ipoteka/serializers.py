from rest_framework import serializers


class MortgageOffersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payment = serializers.IntegerField()
    bank_name = serializers.CharField()
    term_min = serializers.IntegerField() # Срок ипотеки, ОТ
    term_max = serializers.IntegerField() # Срок ипотеки, ДО
    rate_min = serializers.FloatField() # Ставка, ОТ
    rate_max = serializers.FloatField() # Ставка, ДО
    payment_min = serializers.IntegerField() # Сумма кредита, ОТ
    payment_max = serializers.IntegerField() # Сумма кредита, ДО