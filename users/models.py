from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager


class User(AbstractUser):
    username = None
    telegram = models.CharField(max_length=30,  unique=True, verbose_name='телеграмм')
    email = models.EmailField(max_length=30, unique=True, verbose_name="Почта")
    chat_id = models.CharField(max_length=30, verbose_name='telegram_1chat_id', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
