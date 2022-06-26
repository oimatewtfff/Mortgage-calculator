from rest_framework import viewsets
from .models import MortgageOffers
from .serializers import MortgageOffersSerializer


class MortgageOffersViewSet(viewsets.ModelViewSet):
    queryset = MortgageOffers.objects.all()
    serializer_class = MortgageOffersSerializer
