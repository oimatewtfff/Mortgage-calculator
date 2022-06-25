from rest_framework import fields, serializers
from .models import MortgageOffers


class MortgageOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageOffers
        fields = ('id','payment','bank_name','term_min','term_max','rate_min','rate_max','payment_min','payment_max')