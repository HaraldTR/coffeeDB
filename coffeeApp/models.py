from django.db import models


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

class RoastedCoffee(models.Model):
    """
    A model for a roasted coffee.
    """

    coffee_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=400)
    price_per_kg_nok = models.IntegerField()
    roast_date = models.DateField()
#    batch_fk = models.ForeignKey(CoffeeDrinker, on_delete=models.CASCADE, null=True, related_name="coffeedrinker")
    # roastery_fk

    class Meta:
        db_table = 'roasted_coffee'

    def __str__(self):
        return f'Coffee ID: {self.coffee_id}.\n ({self.description})'


class CoffeeTasting(models.Model):
    """
    A tasting of a coffee done by a user.
    """

    tastingID = models.BigAutoField(primary_key=True)
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