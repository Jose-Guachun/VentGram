#django
from django.db import models

#utilities
from utils.models import CRideModel
from users.models import User

#validators
from django.core import validators
from VentGram.validators import SoloNumeros


def ruta_imagen_Category(instance, file_name):
    route='{}/{}/{}'.format( 'category', instance.category, file_name)
    return route

def ruta_imagen_Status(instance, file_name):
    route='{}/{}/{}'.format( 'status', instance.status, file_name)
    return route
class Category(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    category=models.CharField(max_length=60, validators=[validators.MinLengthValidator(5)])
    image=models.ImageField(upload_to=ruta_imagen_Category)
    

    def __str__(self):
        #return username
        return str(self.category)

class Status(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    status=models.CharField(max_length=30, validators=[validators.MinLengthValidator(5)])
    image=models.ImageField(upload_to=ruta_imagen_Status)

    def __str__(self):
        #return username
        return str(self.status)