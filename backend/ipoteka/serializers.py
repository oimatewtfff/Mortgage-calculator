from rest_framework import fields, serializers
from .models import MortgageOffers


class MortgageOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageOffers
        fields = ('bank_name', 'mortgage_rate', 'mortgage_payment')