from django.shortcuts import render
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status, permissions, generics
from .serializers import RestaurantSerializer, MenuSerializer, MyMapSerializer
from .models import Restaurant, My_Map, Menu
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class RestaurantSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#레스토랑 생성
restaurant_create = RestaurantSet.as_view({
    'post' : 'create',
})

#레스토랑 조회, 업데이트, 삭제
restaurant_detail = RestaurantSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy',
})


#메뉴 조회
class RetrieveMenu(generics.RetrieveAPIView):

    def get(self):
        pass
        #menu =Menu.objects.filter(menu_restaurant = )
        #serializer = MenuSerializer()
        #django-filter 알아보기

#나의 맛집 지도 생성
class CreateMyMapAPI(APIView):
    pass

#나의 맛집 지도 조회
class RetrieveMyMapAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        mymap = My_Map.objects.filter(my_id=request.user)
        serializer_class = MyMapSerializer(mymap, many=True)
        print(request.user)
        return Response({"mymap":serializer_class.data})