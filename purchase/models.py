from django.db import models
from shop.models import Product


class Purchase(models.Model):
    created = models.DateTimeField('создано', auto_now_add=True)
    updated = models.DateTimeField('отредактировано', auto_now=True)
    processed = models.BooleanField('обработано', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', verbose_name='заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', null=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
