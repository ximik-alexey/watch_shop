from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='клиент', on_delete=models.CASCADE)
    phone_number = models.CharField('номер телефона', max_length=12, null=True)
    date_of_birth = models.DateField('день рождения',blank=True, null=True)
    purchase_number = models.IntegerField('количество покупок', null=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
