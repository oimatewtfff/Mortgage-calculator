from rest_framework import serializers
from .models import MortgageOffers


class MortgageOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageOffers
        fields = ('bank_name',
                  'rate_min',
                  'rate_max',
                  'term_min',
                  'term_max',
                  'payment_min',
                  'payment_max')
