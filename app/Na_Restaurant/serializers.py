from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import authenticate
from .models import Restaurant, My_Map
from members.serializers import UserSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MyMapRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'restaurant_name',
            'restaurant_address',
        )

class MyMapSerializer(ModelSerializer):
    my_id = UserSerializer(read_only=True)
    my_restaurant = MyMapRestaurantSerializer(read_only=True)
    class Meta:
        model = My_Map
        fields = '__all__'