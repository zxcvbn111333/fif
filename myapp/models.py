from django.db import models






class water(models.Model):
    name = models.CharField(max_length=200,verbose_name="Имя")
    color = models.CharField(max_length=222,verbose_name="Цвет")
    cost = models.IntegerField(verbose_name="Стоимость")
    count = models.IntegerField(verbose_name="Количество")
    volume = models.IntegerField(verbose_name="Обьем")
    pic = models.ImageField(upload_to="myapp/static/", blank=True)


    def __str__(self):
        return self.name


# Create your models here.
