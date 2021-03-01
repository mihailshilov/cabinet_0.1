from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from newcars.models import NewCar
from newcars.serializers import NewCarSerializer


class NewCarViewSet(ModelViewSet):
    queryset = NewCar.objects.all()
    serializer_class = NewCarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['price']
    search_fields = ['vin', 'model']
    ordering_fields = ['price']


def auth(request):
    return render(request, 'oauth.html')
