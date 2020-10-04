#django
from django.db import models

#utilities
from utils.models import CRideModel
from users.models import User

#validators
from django.core import validators
from users.validators import SoloNumeros

class Category(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    category=models.CharField(max_length=60, validators=[validators.MinLengthValidator(5)])
    image=models.ImageField(upload_to='category/photos/%Y/%m/%d/')
    

    def __str__(self):
        #return username
        return str(self.category)