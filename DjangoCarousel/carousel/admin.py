from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import *

@admin.register(CarouselModel)
class CarouselModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "preview", "my_order")
    ordering = ("my_order",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.picture:
            return mark_safe(f"<img src='{obj.picture.url}' style='max-height: 90px;'>")

    preview.short_description = "Миниатюра"
