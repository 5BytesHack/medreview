import datetime

from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fio = models.CharField(verbose_name='ФИО', max_length=128)
    mail = models.EmailField(verbose_name='Адрес для отправки ответа')
    text = models.TextField(verbose_name='Текст обращения')
    reviewed = models.BooleanField(verbose_name='Просмотрено', default=False)


class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField()
