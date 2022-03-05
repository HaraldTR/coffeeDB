from rest_framework import filters
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response

from . import models
from . import serializers


class CoffeeDrinkerView(viewsets.ModelViewSet):
    """
    View for CoffeeDrinker model
    """
    serializer_class = serializers.CoffeeDrinkerSerializer
    queryset = models.CoffeeDrinker.objects.all()

class CoffeeTastingView(viewsets.ModelViewSet):
    """
    View for CoffeeDrinker model
    """
    serializer_class = serializers.CoffeeTastingSerializer
    queryset = models.CoffeeTasting.objects.all()

class RoastedCoffeeView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """
    serializer_class = serializers.RoastedCoffeeSerializer
    queryset = models.RoastedCoffee.objects.all()

