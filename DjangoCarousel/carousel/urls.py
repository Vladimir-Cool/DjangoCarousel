from django.urls import path

from .views import get_home_page_with_carousel

urlpatterns = [
    path('', get_home_page_with_carousel, name="home"),
]