from django.db import models

# Create your models here.
class Direction(models.Model):
    address = models.CharField(max_length =260)
    longitude = models.FloatField(null = True)
    latitude = models.FloatField(null =True)
