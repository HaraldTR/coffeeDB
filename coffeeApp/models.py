from django.db import models

class ProcessingType(models.Model):
    """
    A type of processing method for a coffee bean.
    """

    processing_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    class Meta:
        db_table = 'processing_type' 

    def __str__(self):
        return f'{self.name}'

class CoffeeFarm(models.Model):
    """
    A coffee farm.
    """

    coffee_farm_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    meters_above_sea = models.IntegerField()
    region = models.CharField(max_length=400)
    country = models.CharField(max_length=400)

    class Meta:
        db_table = 'coffee_farm'    

    def __str__(self):
        return f'{self.name}'

class UnprocessedBean(models.Model):
    """
    An unprocesesed coffee bean.
    """

    unprocessed_bean_id = models.BigAutoField(primary_key=True)
    species = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'unprocessed_coffee_bean'

    def __str__(self):
        return f'{self.species}'

class CoffeeBatch(models.Model):
    """
    A batch of coffee beans from a farm.
    """

    batch_id = models.BigAutoField(primary_key=True)
    harvest_year = models.DateField()
    price_pr_kg_usd = models.IntegerField()

    # Get all unprocessed beans in this batch
    unprocessed_beans = models.ManyToManyField(UnprocessedBean)
    
    # FKs to get processing type and farms
    processing_type = models.ForeignKey(ProcessingType, on_delete=models.CASCADE, null=True, related_name="processing_type")
    coffee_farm = models.ForeignKey(CoffeeFarm, on_delete=models.CASCADE, null=True, related_name="coffeefarm")

    class Meta:
        db_table = 'coffee_batch'
    
    def __str__(self):
        return f'harvest year: {self.harvest_year} \nFarm: {self.coffee_farm}'

class RoastedCoffee(models.Model):
    """
    A model for a roasted coffee.
    """

    coffee_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=400)
    price_per_kg_nok = models.IntegerField()
    roast_date = models.DateField()

    #TODO add roastery and roast grade
    batch = models.ForeignKey(CoffeeBatch, on_delete=models.CASCADE, null=True, related_name="coffeebatch")
    
    class Meta:
        db_table = 'roasted_coffee'

    def __str__(self):
        return f'Coffee ID: {self.coffee_id}.\n ({self.description})'

#! TODO hvordan lage join-tabeller og gjøre reverse lookups?
class CoffeeDrinker(models.Model):
    """
    A model for a coffee drinker.
    """

    userID = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'coffee_drinker'

    def __str__(self):
        return f'{self.full_name} with userID ({self.userID})'

class CoffeeTasting(models.Model):
    """
    A tasting of a coffee done by a user.
    """

    tasting_id = models.BigAutoField(primary_key=True)
    notes = models.CharField(max_length=400)
    score = models.IntegerField()
    taste_date = models.DateField()
    # coffee_id = 
    user_id_fk = models.ForeignKey(CoffeeDrinker, on_delete=models.CASCADE, null=True, related_name="coffeedrinker")
    coffee_id_fk = models.ForeignKey(RoastedCoffee, on_delete=models.CASCADE, null=True, related_name="roastedcoffee")


    class Meta:
        db_table = 'coffee_tasting'

    def __str__(self):
        return f'Tasting ID: {self.tastingID} with score ({self.score})'