from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MortgageOffers
from .serializers import MortgageOffersSerializer


class MortgageOffersAPIView(APIView):
    def get(self, request):
        offers = MortgageOffers.objects.all()
        return Response({'offer': MortgageOffersSerializer(offers, many=True).data})

    def post(self, request):
        offer_new = MortgageOffers.objects.create(
            bank_name=request.data['bank_name'],
            term_min=request.data['term_min'],
            term_max=request.data['term_max'],
            rate_min=request.data['rate_min'],
            rate_max=request.data['rate_max'],
            payment_min=request.data['payment_min'],
            payment_max=request.data['payment_max']
        )
        return Response({'offer': MortgageOffersSerializer(offer_new).data})
    