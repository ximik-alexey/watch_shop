# Generated by Django 3.0.6 on 2020-05-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_phone_number_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='secret_user_token',
            field=models.CharField(max_length=6, null=True, verbose_name='токен подтверждения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_phone_number_verified',
            field=models.BooleanField(default=False, verbose_name='верификация'),
        ),
    ]