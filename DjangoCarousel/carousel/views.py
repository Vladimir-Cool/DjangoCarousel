from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def get_home_page_with_carousel(request: HttpRequest) -> HttpResponse:
    """ Функция венрен домашнюю страницу с 'каруселью' картинок"""
    # Забрать контекст из модели
    context = {"data": "Тут будет Data"}
    return render(request, "carousel/carousel.html", context=context)