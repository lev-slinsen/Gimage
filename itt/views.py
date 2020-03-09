from rest_framework.permissions import AllowAny

from .models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['post']
