# Generated by Django 3.0.6 on 2020-06-03 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200602_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='glass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glass', to='shop.Glass', verbose_name='стекло'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mechanism_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanism_type', to='shop.MechanismType', verbose_name='тип механизма'),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_resistance_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water', to='shop.WaterResistanceClass', verbose_name='влагозащита'),
        ),
    ]