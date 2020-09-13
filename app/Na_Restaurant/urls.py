from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateMyMapAPI, RetrieveMyMapAPI
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant', views.restaurant_create),
    path('restaurant/<int:pk>', views.restaurant_detail),
    path('mymap', RetrieveMyMapAPI.as_view()),
    path('ca/<int:pk>', views.category_detail),
]