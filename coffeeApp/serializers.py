from rest_framework import serializers
from .models import *

class CoffeeDrinkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeDrinker
        fields = '__all__'

class ProcessingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingType
        fields = '__all__'

class CoffeeFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeFarm
        fields = '__all__'

class UnprocessedBeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnprocessedBean
        fields = '__all__'

class CoffeeBatchListSerializer(serializers.ModelSerializer):

    processing_type = ProcessingTypeSerializer()
    unprocessed_beans = UnprocessedBeanSerializer(many=True)
    processing_type = ProcessingTypeSerializer()
    coffee_farm = CoffeeFarmSerializer()

    class Meta:
        model = CoffeeBatch
        fields='__all__'

class CoffeeBatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeBatch
        fields='__all__'

class RoastedCoffeUseBatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeBatch
        fields= ['batch_id']

# Serializer for logging in 
class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoffeeDrinker
        fields = ['email', 'password']

class RoastedCoffeeListSerializer(serializers.ModelSerializer):
    
    batch = CoffeeBatchListSerializer()

    class Meta:
        model = RoastedCoffee
        fields = '__all__'

class RoastedCoffeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoastedCoffee
        fields = ['coffee_id', 'description', 'price_per_kg_nok', 'roast_date', 'batch' ]

class CoffeeTastingListSerializer(serializers.ModelSerializer):
    
    coffee_id_fk = RoastedCoffeeListSerializer()

    class Meta:
        model = CoffeeTasting
        fields = '__all__'

class CoffeeTastingCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoffeeTasting
        fields = '__all__'
