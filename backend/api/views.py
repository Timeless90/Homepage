# Views for Sales models

from rest_framework import generics, viewsets
from .models import Customer, DevelopmentModel
from .serializers import CustomerSerializer, DevelopmentModelSerializer

class CustomerList(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DevelopmentModelList(viewsets.ModelViewSet):
    queryset = DevelopmentModel.objects.all()
    serializer_class = DevelopmentModelSerializer