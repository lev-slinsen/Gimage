from rest_framework import serializers
from .models import Image
from django.utils.translation import pgettext_lazy as _


def image_validator(value):
    if len(value) < 2:
        raise serializers.ValidationError(_('Validator|Image', 'This link should lead to an image directly'))


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_url',)
    validators = (image_validator,)
