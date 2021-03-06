# Generated by Django 3.1.7 on 2021-02-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=20, verbose_name='VIN номер')),
                ('con', models.CharField(max_length=10, verbose_name='CON номер')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('img', models.CharField(max_length=255, verbose_name='Изображение')),
                ('engine', models.CharField(max_length=65, verbose_name='Двигатель')),
                ('fuel_type', models.CharField(max_length=65, verbose_name='Тип топлива')),
                ('compl', models.CharField(max_length=65, verbose_name='Комплектация')),
                ('model', models.CharField(max_length=65, verbose_name='Модель')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка')),
            ],
        ),
    ]
