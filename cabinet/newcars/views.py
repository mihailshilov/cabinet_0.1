from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from newcars.models import NewCar
from newcars.serializers import NewCarSerializer


class NewCarViewSet(ModelViewSet):
    queryset = NewCar.objects.all()
    serializer_class = NewCarSerializer
