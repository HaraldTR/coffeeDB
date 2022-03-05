from rest_framework import serializers
from .models import CoffeeDrinker, CoffeeTasting, RoastedCoffee

class CoffeeDrinkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeDrinker
        fields = '__all__'

class CoffeeTastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeTasting
        fields = '__all__'

class RoastedCoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoastedCoffee
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoffeeDrinker
        fields = ['email', 'password']
