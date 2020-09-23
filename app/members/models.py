from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField('nickname', max_length=30, unique=True)
    user_region = models.CharField(max_length=50, null=True, blank=True)