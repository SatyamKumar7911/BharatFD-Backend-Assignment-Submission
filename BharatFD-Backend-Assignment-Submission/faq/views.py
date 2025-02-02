from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(settings.CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

