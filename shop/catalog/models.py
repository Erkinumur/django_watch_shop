from django.db import models
from django.urls import reverse

from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Watch(models.Model):
    title = models.CharField(max_length=50, verbose_name='Модель')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='watchs', verbose_name='Брэнд')
    group = models.ManyToManyField(Group, related_name='watchs', verbose_name='Котегория')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Фото')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('watch_detail', args=[self.pk])