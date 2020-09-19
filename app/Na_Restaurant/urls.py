from django.conf.urls import url
from .views import CreateMyMapAPI, RetrieveMyMapAPI, DestroyMyMapAPI, RetrieveMenuAPI, CreateMenuAPI, DestroyMenuAPI
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant', views.restaurant_create),
    path('restaurant/<int:pk>', views.restaurant_detail),
    path('menu/create/<int:restaurant_id>', CreateMenuAPI.as_view()),
    path('menu/<restaurant_id>', RetrieveMenuAPI.as_view()),
    path('mymap', RetrieveMyMapAPI.as_view()),
    path('cmymap', CreateMyMapAPI.as_view()),
    url(r'^(?P<pk>\d+)/deletemymap/$', DestroyMyMapAPI.as_view()),
    url(r'^(?P<pk>\d+)/deletemenu/$', DestroyMenuAPI.as_view()),
    path('ca/<int:pk>', views.category_detail),
]