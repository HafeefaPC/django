from django.db import models

# Create your models here.


class Tour(models.Model):
    #we need origin  country destination,number of nights, price
    #blueprint for the database
    origin_country =models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    #this is a string representation of Tour in general
    def __str__ (self):
        return (f"ID:{self.id}: From {self.origin_country} to {self.destination_country}, {self.number_of_nights} nights costs ${self.price}")  