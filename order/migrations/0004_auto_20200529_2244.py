# Generated by Django 3.0.6 on 2020-05-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200529_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order_processed',
        ),
        migrations.AddField(
            model_name='order',
            name='order_processed',
            field=models.BooleanField(default=False),
        ),
    ]
