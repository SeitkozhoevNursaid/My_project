# Generated by Django 5.0.1 on 2024-01-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_list_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_list',
            name='price',
            field=models.CharField(max_length=50, verbose_name='Цена Товара'),
        ),
    ]
