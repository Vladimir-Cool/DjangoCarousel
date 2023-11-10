from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import CarouselModel

def get_home_page_with_carousel(request: HttpRequest) -> HttpResponse:
    """ Функция венрен домашнюю страницу с 'каруселью' картинок"""
    # Забрать контекст из модели

    query_set = CarouselModel.objects.all()

    context = {"data": "Тут будет Data"}
    return render(request, "carousel/carousel.html", context={"data": query_set})