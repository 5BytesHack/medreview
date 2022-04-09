import datetime

import jwt.api_jwt
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings

from .managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=40)
    last_name = models.CharField(verbose_name='Фамилия', max_length=40)
    patronymic = models.CharField(verbose_name='Отчество', max_length=40, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    @property
    def token(self):
        return self._generate_jwt()

    def get_full_name(self):
        if self.patronymic:
            return f'{self.last_name} {self.first_name} {self.patronymic}'
        else:
            return f'{self.last_name} {self.first_name}'

    def _generate_jwt(self):
        dt = datetime.datetime.now() + datetime.timedelta(days=7)
        token = jwt.api_jwt.encode({
            'id': self.pk,
            'exp': dt,
        }, settings.SECRET_KEY, algorithm='HS256')
        return token
