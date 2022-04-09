# Generated by Django 4.0.3 on 2022-04-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=128, verbose_name='ФИО')),
                ('mail', models.EmailField(max_length=254, verbose_name='Адрес для отправки ответа')),
                ('text', models.TextField(verbose_name='Текст обращения')),
                ('reviewed', models.BooleanField(default=False, verbose_name='Просмотрено')),
            ],
        ),
    ]
