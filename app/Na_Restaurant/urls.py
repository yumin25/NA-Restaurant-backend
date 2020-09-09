from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateMyMapAPI
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'MyMap', views.MyMapSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant', views.restaurant_create),
    path('restaurant/<int:pk>', views.restaurant_detail),
]