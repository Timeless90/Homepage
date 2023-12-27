# Serializer for sales models

from rest_framework import serializers
from .models import Customer, DevelopmentModel

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'namestyle',
            'title',
            'firstname',
            'middlename',
            'lastname',
            'suffix',
            'companyname',
            'salesperson',
            'emailaddress',
            'phone',

        ]

class DevelopmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentModel
        fields = [
            'name',
            'description',
            'created_at',
            'updated_at',
        ]