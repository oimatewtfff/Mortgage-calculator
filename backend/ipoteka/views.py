from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import MortgageOffers
from .serializers import MortgageOffersSerializer


class MortgageFilter(filters.FilterSet):
    price = filters.NumberFilter(field_name="payment_min", lookup_expr='lte')
    # deposit = filters.NumberFilter(field_name="payment")  # TODO 
    term = filters.NumberFilter(field_name="term_min", lookup_expr='lte')

    # def get_past_n_hours(self, queryset, field_name, value):
    #     time_threshold = timezone.now() - timedelta(hours=int(value))
    #     return queryset.filter(time_stamp__gte=time_threshold)

    class Meta:
        model = MortgageOffers
        fields = []


class MortgageOffersViewSet(viewsets.ModelViewSet):
    queryset = MortgageOffers.objects.all()
    serializer_class = MortgageOffersSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MortgageFilter
    ordering_fields = ['rate_min']
