from django.db import models
from django.utils.translation import pgettext_lazy as _


class Image(models.Model):
    image_url = models.URLField(max_length=1000, verbose_name=_('itt|Image url', 'Image url'))
