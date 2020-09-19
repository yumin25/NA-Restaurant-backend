from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Restaurant, Menu, My_Map, Categories
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

class MenuSerializer(serializers.ModelSerializer):
    #menu_restaurant = MyMapRestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = (
            'menu_id',
            'menu_name',
            'menu_price',
        )

class CategorySerializer(ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Categories
        fields = '__all__'


class MyMapSerializer(ModelSerializer):
    my_restaurant = MyMapRestaurantSerializer(read_only=True)
    class Meta:
        model = My_Map
        fields = (
            'my_restaurant',
        )

class CreateMyMapSerializer(ModelSerializer):
    my_id = UserSerializer(read_only=True)
    class Meta:
        model = My_Map
        fields = '__all__'