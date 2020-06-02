from django.db import models
from shop.models import Product


class Storehouse(models.Model):
    name = models.CharField('имя поставшика', max_length=50)
    created = models.DateTimeField('создано', auto_now_add=True)
    updated = models.DateTimeField('отредактировано', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'поставка'
        verbose_name_plural = 'поставки'


class StorehouseItem(models.Model):
    storehouse = models.ForeignKey(Storehouse, related_name='items', verbose_name='заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='storehouse_items', verbose_name='продукт',
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', null=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        name = self.product
        obj = StorehouseItem.objects.filter(product=name).values("quantity")
        number = 0
        for i in obj:
            number += i["quantity"]
        product = Product.objects.get(name=name)
        product.quantity += number
        product.save()
        return

    def delete(self, using=None, keep_parents=False):
        name = self.product.name
        product = Product.objects.get(name=name)
        product.quantity -= self.quantity
        product.save()
        super().delete()
        return
