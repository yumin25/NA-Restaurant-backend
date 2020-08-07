from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    emailname = models.EmailField('email', max_length=50, unique=True)
    pass