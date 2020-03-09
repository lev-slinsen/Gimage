from django.db import models
from django.utils.translation import pgettext_lazy as _
from google.cloud import vision
from rest_framework import serializers


class Image(models.Model):
    image_uri = models.URLField(max_length=1000, verbose_name=_('itt|Image url', 'Image url'))

    @property
    def get_obj_list(self):
        client = vision.ImageAnnotatorClient()

        image = vision.types.Image()
        image.source.image_uri = self.image_uri

        objects = client.object_localization(
            image=image).localized_object_annotations

        obj_list = []
        for object_ in objects:
            obj_list.append(object_.name)
        obj_list.sort()
        if len(obj_list) == 0:
            raise serializers.ValidationError(_('Validator|Image', 'No objects were found at this link'))

        return obj_list

    def __str__(self):
        return f'Image # {self.id}'
