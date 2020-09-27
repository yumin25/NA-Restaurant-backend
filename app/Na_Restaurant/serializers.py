from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Restaurant, Menu, My_Map, Category, Review_Local, Review_Other
from members.serializers import UserSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class PreviewRestaurantSerializer(serializers.ModelSerializer):
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
        model = Category
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

class Create_Review_Local_Serializer(ModelSerializer):
    review_user = UserSerializer(read_only=True)

    class Meta:
        model = Review_Local
        fields = (
            'review_user',
            'review_menu',
            'review_restaurant',
            'review_title',
            'review_text',
            'review_star',
        )


class Create_Review_Other_Serializer(ModelSerializer):
    review_user = UserSerializer(read_only=True)

    class Meta:
        model = Review_Other
        fields = (
            'review_user',
            'review_menu',
            'review_restaurant',
            'review_title',
            'review_text',
            'review_star',
        )

class Review_Local_Serializer(ModelSerializer):
    review_user = UserSerializer(read_only=True)
    review_menu = MenuSerializer(read_only=True)
    class Meta:
        model = Review_Local
        fields = '__all__'


class Review_Other_Serializer(ModelSerializer):
    review_user = UserSerializer(read_only=True)
    review_menu = MenuSerializer(read_only=True)
    class Meta:
        model = Review_Other
        fields = '__all__'