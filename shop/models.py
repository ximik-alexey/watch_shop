from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField('бренд', max_length=200, db_index=True)
    slug = models.SlugField('url бренд', max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'

    def __str__(self):
        return self.name


class Glass(models.Model):
    name = models.CharField('тип стекла', max_length=200)
    slug = models.SlugField('url стекла', max_length=200, unique=True)

    class Meta:
        verbose_name = 'стекло'
        verbose_name_plural = 'стекло'

    def __str__(self):
        return self.name


class MechanismType(models.Model):
    name = models.CharField('тип механизма', max_length=200)
    slug = models.SlugField('url', max_length=200, unique=True)

    class Meta:
        verbose_name = 'тип механизма'
        verbose_name_plural = 'тип механизма'

    def __str__(self):
        return self.name


class WaterResistanceClass(models.Model):
    name = models.CharField('влагозащита', max_length=200)
    slug = models.SlugField('url влагозащиты', max_length=200, unique=True)

    class Meta:
        verbose_name = 'влагозащита'
        verbose_name_plural = 'влагозащита'

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, related_name='products', verbose_name='бренд', on_delete=models.CASCADE)
    name = models.CharField('имя', max_length=200, db_index=True)
    slug = models.SlugField('url продукта', max_length=200, db_index=True)
    image = models.ImageField('изображение', upload_to='shop/templates/img', blank=True)
    description = models.TextField('описание', blank=True)
    glass = models.ForeignKey(Glass, related_name='products', verbose_name='стекло', on_delete=models.CASCADE)
    dimension = models.CharField('размер', max_length=200, null=True)
    water_resistance_class = models.ForeignKey(WaterResistanceClass, related_name='products',
                                               verbose_name='влагозащита', on_delete=models.CASCADE)
    mechanism_type = models.ForeignKey(MechanismType, related_name='products',
                                       verbose_name='тип механизма', on_delete=models.CASCADE)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('количество')
    stock = models.PositiveIntegerField('остатки')
    available = models.BooleanField('доступность', default=True)
    created = models.DateTimeField('создано', auto_now_add=True)
    updated = models.DateTimeField('отредактировано', auto_now=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stock == 0:
            self.available = False
        if self.stock != 0:
            self.available = True
        return super().save()

