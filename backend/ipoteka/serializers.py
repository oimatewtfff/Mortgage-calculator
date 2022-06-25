from rest_framework import serializers
from .models import MortgageOffers


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

    def create(self, validated_data):
        return MortgageOffers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bank_name = validated_data.get('bank_name', instance.bank_name)
        instance.term_min = validated_data.get('term_min', instance.term_min)
        instance.term_max = validated_data.get('term_max', instance.term_max)
        instance.rate_min = validated_data.get('rate_min', instance.rate_min)
        instance.rate_max = validated_data.get('rate_max', instance.rate_max)
        instance.payment_min = validated_data.get('payment_min', instance.payment_min)
        instance.payment_max = validated_data.get('payment_max', instance.payment_max)
        instance.save()
        return instance