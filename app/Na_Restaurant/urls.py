from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateRestaurantAPI, UpdateRestaurantAPI, DestroyRestaurantAPI, RetrieveRestaurantAPI

urlpatterns = format_suffix_patterns([
    url("^createrestaurant/$", CreateRestaurantAPI.as_view()),
    url(r'^(?P<pk>\d+)/updaterestaurant/$', UpdateRestaurantAPI.as_view()),
    url(r'^(?P<pk>\d+)/destroyrestaurant/$', DestroyRestaurantAPI.as_view()),
    url(r'^(?P<pk>\d+)/retrieverestaurant/$', RetrieveRestaurantAPI.as_view()),
])
