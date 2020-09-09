from django.shortcuts import render
from .serializers import RestaurantSerializer, MyMapSerializer
from rest_framework.generics import UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .models import Restaurant, My_Map
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class RestaurantSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

restaurant_create = RestaurantSet.as_view({
    'post' : 'create',
})

restaurant_detail = RestaurantSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy',
})

class CreateMyMapAPI(CreateAPIView):
    #queryset = My_Map.objects.get(my_id = user.get_username())
    serializer_class = MyMapSerializer

class RetrieveMyMapAPI(RetrieveAPIView):
    queryset = My_Map.objects.all()
    serializer_class = MyMapSerializer

class MyMapSet(ModelViewSet):
    queryset = My_Map.objects.all()
    serializer_class = MyMapSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(my_id=self.request.user)