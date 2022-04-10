import datetime

from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fio = models.CharField(verbose_name='ФИО', max_length=128)
    mail = models.EmailField(verbose_name='Адрес для отправки ответа')
    text = models.TextField(verbose_name='Текст обращения')
    title = models.BooleanField(verbose_name='Тема обращения')
    date = models.DateField(verbose_name='Дата обращения', auto_now=True)

    def get_email(self):
        return self.mail


class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст ответа')
    date = models.DateField(verbose_name='Дата ответа', auto_now=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
