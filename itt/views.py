from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ('post',)
    permission_classes = (AllowAny,)
