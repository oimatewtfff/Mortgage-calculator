from signal import raise_signal
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from .models import MortgageOffers
from .serializers import MortgageOffersSerializer


class MortgageOffersAPIView(APIView):
    def get(self, request):
        offers = MortgageOffers.objects.all()
        return Response({'offer': MortgageOffersSerializer(offers, many=True).data})

    def post(self, request):
        serializer = MortgageOffersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'offer': serializer.data})
    
    def patch(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        if not id:
            return Response({'error': 'Method put not allowed'})

        try:
            instance = MortgageOffers.objects.get(id=id)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = MortgageOffersSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'offer': serializer.data})
