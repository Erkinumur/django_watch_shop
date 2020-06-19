from django.db import models
from catalog.models import Watch
from django.urls import reverse


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.id}'

    def get_absolute_url(self):
        return reverse('order_detail', args=[self.pk])

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity