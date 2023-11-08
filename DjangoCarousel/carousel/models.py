from django.db import models

class CarouselModel(models.Model):
    name = models.CharField("название", max_length=100)
    picture = models.FilePathField(path="carousel/static/img")


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
