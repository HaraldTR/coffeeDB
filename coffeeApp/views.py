from rest_framework import filters
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from django.http import JsonResponse

from . import models
from . import serializers
from rest_framework import generics

class LoginView(viewsets.ModelViewSet):
    """
    View for CoffeeDrinker model
    """
    serializer_class = serializers.LoginSerializer
    queryset = models.CoffeeDrinker.objects.all()

    def list(self, request):
        return Response('Please enter your credentials to login')

    def create(self, request):
        user_email = self.request.data['email']
        user_password = self.request.data['password']

        # Ugly, but gets the login data from the request
        is_login = list(models.CoffeeDrinker.objects.filter(email=user_email).filter(password=user_password).values())
                
        if is_login:
            return Response(f'Welcome {is_login[0]["full_name"]}. Go to THIS LINK to use the app.') 
        else:
            return Response('Wrong credentials.')

class RegisterView(viewsets.ModelViewSet):
    """
    View for CoffeeDrinker model
    """
    serializer_class = serializers.CoffeeDrinkerSerializer
    queryset = models.CoffeeDrinker.objects.all()

    def list(self, request):
        return Response('Create a new user.')

class ProcessingTypeView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """
    serializer_class = serializers.ProcessingTypeSerializer
    queryset = models.ProcessingType.objects.all()


class CoffeeFarmView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """
    serializer_class = serializers.CoffeeFarmSerializer
    queryset = models.CoffeeFarm.objects.all()

class UnprocessedBeanView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """
    serializer_class = serializers.UnprocessedBeanSerializer
    queryset = models.UnprocessedBean.objects.all()

class CoffeeBatchView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CoffeeBatchListSerializer
        if self.action == 'create':
            return serializers.CoffeeBatchSerializer
    
    queryset = models.CoffeeBatch.objects.all()

class RoastedCoffeeView(viewsets.ModelViewSet):
    """
    View for RoastedCoffee model
    """

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RoastedCoffeeListSerializer
        if self.action == 'create':
            return serializers.RoastedCoffeeCreateSerializer

    queryset = models.RoastedCoffee.objects.all()

class CoffeeTastingView(viewsets.ModelViewSet):
    """
    View for CoffeeDrinker model
    """

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CoffeeTastingListSerializer
        if self.action == 'create':
            return serializers.CoffeeTastingCreateSerializer

    queryset = models.CoffeeTasting.objects.all()