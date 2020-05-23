# Generated by Django 3.0.6 on 2020-05-23 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_profile_purchase_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'профиль', 'verbose_name_plural': 'профили'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='purchase_number',
            field=models.IntegerField(null=True, verbose_name='количество покупок'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='клиент'),
        ),
    ]
