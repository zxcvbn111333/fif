# Generated by Django 5.0.6 on 2024-06-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='pic',
            field=models.ImageField(blank=True, upload_to='myapp/static/'),
        ),
        migrations.AlterField(
            model_name='water',
            name='color',
            field=models.CharField(max_length=222, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='water',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='water',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='water',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='water',
            name='volume',
            field=models.IntegerField(verbose_name='Обьем'),
        ),
    ]
