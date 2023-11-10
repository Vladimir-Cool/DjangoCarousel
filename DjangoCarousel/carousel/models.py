from django.db import models

class CarouselModel(models.Model):
    name = models.CharField("Название", max_length=100)
    picture = models.ImageField("Изображение")
    my_order = models.PositiveIntegerField("Сартировка", default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
