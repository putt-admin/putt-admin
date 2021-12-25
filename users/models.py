from django.db import models

from django.contrib.auth.models import AbstractUser
from .queryset import EnhancedUserManager


class User(AbstractUser):

    objects = EnhancedUserManager()
