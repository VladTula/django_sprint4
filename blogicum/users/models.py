from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)
