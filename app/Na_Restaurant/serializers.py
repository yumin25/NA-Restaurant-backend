from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'