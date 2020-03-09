from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_uri', 'get_obj_list')

    def __init__(self, *args, **kwargs):
        super(ImageSerializer, self).__init__(*args, **kwargs)
        if self.context != {}:
            request = self.context['request']
            if request.method == 'POST':
                self.write_only_fields = ['get_obj_list']
