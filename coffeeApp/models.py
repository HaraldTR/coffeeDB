from django.db import models

# Create your models here.

#! TODO hvordan lage join-tabeller og gjøre reverse lookups?

class CoffeeDrinker(models.Model):
    """A model for a coffee drinker.
    """

    userID = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=40)

    class Meta:
        db_table = 'coffee_drinker'

    def __str__(self):
        return f'{self.full_name} with userID ({self.userID})'