# Generated by Django 3.0.6 on 2020-05-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200530_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]
