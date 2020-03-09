from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image_uri',
    )
    fields = (
        'id',
        'image_uri',
        # 'get_obj_list',
    )
    readonly_fields = (
        'id',
        # 'get_obj_list',
    )
    ordering = ('-id',)
