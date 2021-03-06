from django.shortcuts import render
from rest_framework import request
from rest_framework.response import Response

from rest_framework import status, permissions, generics
from .serializers import RestaurantSerializer, PreviewRestaurantSerializer, MenuSerializer, MyMapSerializer, CategorySerializer, CreateMyMapSerializer, Review_Local_Serializer, Review_Other_Serializer, Create_Review_Local_Serializer, Create_Review_Other_Serializer
from .models import Restaurant, My_Map, Menu, Category, Review_Local, Review_Other
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


#동으로 레스토랑 조회
class RetrieveRestaurantAPI(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer = RestaurantSerializer()

    def get(self, request, restaurant_region):
        queryset = Restaurant.objects.filter(restaurant_region = restaurant_region)
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)


#레스토랑 preview
class RetrievePreviewRestaurantAPI(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer = PreviewRestaurantSerializer()

    def get(self, request, restaurant_id):
        queryset = Restaurant.objects.filter(restaurant_id = restaurant_id)
        serializer = PreviewRestaurantSerializer(queryset, many=True)
        return Response(serializer.data)


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

class CategorySet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request):
        restaurant_id = request.GET.get('restaurant_id', None)
        Category.objects.all()

category_detail = CategorySet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy',
})

#메뉴 생성
class CreateMenuAPI(generics.CreateAPIView):

    def post(self, request, restaurant_id):
        serializer_class = MenuSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(menu_restaurant_id = restaurant_id)
            return Response(serializer_class.data, status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

#메뉴 조회
class RetrieveMenuAPI(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer = MenuSerializer()

    def get(self, request, restaurant_id):
        queryset = Menu.objects.filter(menu_restaurant_id = restaurant_id)
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

#메뉴 삭제
class DestroyMenuAPI(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#나의 맛집 지도 생성 CreateMyMapSerializer
class CreateMyMapAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        serializer_class = CreateMyMapSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(my_id = self.request.user)
            return Response(serializer_class.data, status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

#나의 맛집 지도 조회
class RetrieveMyMapAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        mymap = My_Map.objects.filter(my_id=request.user)
        serializer_class = MyMapSerializer(mymap, many=True)
        print(request.user)
        return Response(serializer_class.data)


#나의 맛집 지도 삭제
class DestroyMyMapAPI(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = My_Map.objects.all()
    serializer_class = MyMapSerializer

#카테고리 조회
#class CategoryAPI(generics.RetrieveAPIView):

    #def get(self, request):
        #pass
        #serializer_class = CategorySerializer(Categories, many=True)


#현지인 리뷰 조회
class RetrieveLocalReviewAPI(generics.RetrieveAPIView):
    queryset = Review_Local.objects.all()
    serializer = Review_Local_Serializer()

    def get(self, request, restaurant_id):
        queryset = Review_Local.objects.filter(review_restaurant = restaurant_id)
        serializer = Review_Local_Serializer(queryset, many=True)
        return Response(serializer.data)


#외부인 리뷰 조회
class RetrieveOtherReviewAPI(generics.RetrieveAPIView):
    queryset = Review_Other.objects.all()
    serializer = Review_Other_Serializer()

    def get(self, request, restaurant_id):
        queryset = Review_Other.objects.filter(review_restaurant = restaurant_id)
        serializer = Review_Other_Serializer(queryset, many=True)
        return Response(serializer.data)

#리뷰 생성
class CreateReviewAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        data = self.request.data.copy()
        restaurant = data['review_restaurant']
        queryset = Restaurant.objects.get(restaurant_id = restaurant)

        if self.request.user.user_region == queryset.restaurant_region:
            serializer_class = Create_Review_Local_Serializer(data=request.data)
        else:
            serializer_class = Create_Review_Other_Serializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save(review_user=self.request.user)
            return Response(serializer_class.data, status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)