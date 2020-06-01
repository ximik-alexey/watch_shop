from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя клиента')
    address = models.CharField(max_length=250, verbose_name='адрес доставки')
    city = models.CharField(max_length=100, verbose_name='город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='отредактировано')
    order_processed = models.BooleanField(default=False, verbose_name='заказ обработан')
    phone = models.CharField(max_length=12, null=True, verbose_name='телефон')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', verbose_name='продукт', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')
    limit = models.IntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'состав заказа'
        verbose_name_plural = 'состав заказов'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        name = self.product
        obj = OrderItem.objects.filter(product=name).values("quantity")
        number = 0
        for i in obj:
            number += i["quantity"]
        product = Product.objects.get(name=name)
        if (product.quantity - number) > 0:
            product.stock = product.quantity - number
            self.limit = 0
            product.save()
            super().save()
        else:
            product.stock = 0
            product.save()
            self.limit = product.quantity - number
            super().save()
        return

    def delete(self, using=None, keep_parents=False):
        name = self.product.name
        product = Product.objects.get(name=name)
        product.stock += self.quantity
        product.save()
        super().delete()
