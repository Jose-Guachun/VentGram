#dependencias de django
from django.db import models
from django.conf import settings

#Utilities
from utils.models import CRideModel
from users.models import Profile


class Country(models.Model):
    name_country=models.CharField(max_length=50, blank=True)

    def __str__(self):
    #return name_country
        return self.name_country

class Province(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    name_province=models.CharField(max_length=50, blank=True)

    def __str__(self):
    #return name_provincie
        return self.name_province
    
class City(models.Model):
    province=models.ForeignKey(Province, on_delete=models.CASCADE)
    name_city=models.CharField(max_length=50, blank=True)

    def natural_key(self):
        return (self.name_city)
    
    def __str__(self):
    #return namce_city
        return self.name_city