from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import authenticate
from .models import Restaurant, My_Map

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MyMapSerializer(ModelSerializer):
    class Meta:
        model = My_Map
        fields = '__all__'