from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import get_home_page_with_carousel


urlpatterns = [
    path("", get_home_page_with_carousel, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" Удалить '+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
    При публикации на сервер"""
