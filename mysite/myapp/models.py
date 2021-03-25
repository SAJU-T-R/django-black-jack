from django.db import models

# Create your models here.
class GameBet(models.Model):
    ACCOUNT = models.CharField(max_length=3)

    def __str__(self):
        return self.ACCOUNT

class GameCard(models.Model):
    card_name = models.CharField(max_length=264, db_index=True)

    def __str__(self):
        return self.card_name
