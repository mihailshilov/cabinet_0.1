from django.db import models

# Create your models here.


class NewCar(models.Model):
    vin = models.CharField(max_length=20, verbose_name='VIN номер')
    con = models.CharField(max_length=10, verbose_name='CON номер')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    img = models.CharField(max_length=255, verbose_name='Изображение')
    engine = models.CharField(max_length=65, verbose_name='Двигатель')
    fuel_type = models.CharField(max_length=65, verbose_name='Тип топлива')
    compl = models.CharField(max_length=65, verbose_name='Комплектация')
    model = models.CharField(max_length=65, verbose_name='Модель')
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return f'{self.model} - {self.con}'
