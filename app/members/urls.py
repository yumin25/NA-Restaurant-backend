from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateUserAPI, LoginAPI, UserAPI, UpdateUserAPI
from knox import views as knox_views

urlpatterns = format_suffix_patterns([
    url("^createuser", CreateUserAPI.as_view()),
    url("^login", LoginAPI.as_view()),
    path('user', UserAPI.as_view()),
    path('updateuser/<user_region>', UpdateUserAPI.as_view()),
])