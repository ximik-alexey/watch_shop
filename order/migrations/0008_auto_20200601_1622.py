# Generated by Django 3.0.6 on 2020-06-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderitem_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_processed',
            field=models.BooleanField(default=False, verbose_name='заказ обработан'),
        ),
    ]