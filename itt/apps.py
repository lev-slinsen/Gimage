from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IttConfig(AppConfig):
    name = 'itt'
    verbose_name = _('Image to text')
