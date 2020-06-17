from django.contrib.auth.models import User
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
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Главное фото')
    create_at = models.DateTimeField(auto_now_add=True)

    def get_group(self):
        return ", ".join([str(p) for p in self.group.all()])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('watch_detail', args=[self.pk])


class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='media', verbose_name='Изображение')
    product = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name='Родитель', blank=True, null=True
    )
    watch = models.ForeignKey(Watch, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.watch}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'