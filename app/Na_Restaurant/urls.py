from django.conf.urls import url
from .views import CreateMyMapAPI, RetrieveMyMapAPI, DestroyMyMapAPI, RetrieveMenuAPI, CreateMenuAPI, DestroyMenuAPI, RetrievePreviewRestaurantAPI, RetrieveRestaurantAPI, RetrieveLocalReviewAPI, RetrieveOtherReviewAPI, CreateReviewAPI
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant', views.restaurant_create),
    path('restaurant/<int:pk>', views.restaurant_detail),
    path('restaurant/preview/<int:restaurant_id>', RetrievePreviewRestaurantAPI.as_view()),
    path('restaurant/<restaurant_region>', RetrieveRestaurantAPI.as_view()),
    path('menu/create/<int:restaurant_id>', CreateMenuAPI.as_view()),
    path('menu/<restaurant_id>', RetrieveMenuAPI.as_view()),
    path('mymap', RetrieveMyMapAPI.as_view()),
    path('cmymap', CreateMyMapAPI.as_view()),
    url(r'^(?P<pk>\d+)/deletemymap/$', DestroyMyMapAPI.as_view()),
    url(r'^(?P<pk>\d+)/deletemenu/$', DestroyMenuAPI.as_view()),
    path('ca/<int:pk>', views.category_detail),

    #리뷰
    path('review/create', CreateReviewAPI.as_view()),
    path('review/local/<int:restaurant_id>', RetrieveLocalReviewAPI.as_view()),
    path('review/other/<int:restaurant_id>', RetrieveOtherReviewAPI.as_view()),
]