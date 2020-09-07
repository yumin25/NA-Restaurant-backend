from django.shortcuts import render
from .serializers import RestaurantSerializer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Restaurant

class CreateRestaurantAPI(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantAPI(UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DestroyRestaurantAPI(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RetrieveRestaurantAPI(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer