from django.db import models

# Create your models here.


class Shop_list(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название Товара')
    description = models.CharField(max_length = 250, verbose_name = 'Описание Товара')
    price = models.CharField(max_length = 50,verbose_name = 'Цена Товара')
    image = models.ImageField(upload_to='image/', verbose_name = 'Изображение')
    

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class CartItem(models.Model):
    product = models.ForeignKey(Shop_list, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)