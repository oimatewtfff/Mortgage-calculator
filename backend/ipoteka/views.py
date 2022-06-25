from rest_framework import viewsets

from .models import MortgageOffers
from .serializers import MortgageOffersSerializer


class MortgageOffersViewSet(viewsets.ModelViewSet):
    serializer_class = MortgageOffersSerializer
    queryset = MortgageOffers.objects.all()
    