#django
from django.db import models
from django.conf import settings

#utilities
from utils.models import CRideModel
from django.core import validators
from VentGram.validators import vcedula, SoloNumeros

class Profile(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.OneToOneField('users.User', on_delete=models.CASCADE,)
    city=models.ForeignKey('users.City', on_delete=models.CASCADE, blank=True, null=True)
    
    dni=models.CharField(max_length=10, validators=[validators.MinLengthValidator(10), SoloNumeros], blank=True)
    gender=models.CharField(max_length=20, blank=True)
    birth_date=models.DateField(blank=True, null=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20, validators=[validators.MinLengthValidator(10), SoloNumeros], blank=True)
    education_level=models.CharField(max_length=50, blank=True)
    work_area=models.CharField(max_length=100, blank=True)
    home_address=models.CharField(max_length=100, blank=True)
    facebook=models.URLField(max_length=200, blank=True)
    twitter=models.URLField(max_length=200, blank=True)
    linkedin=models.URLField(max_length=200, blank=True)
    github=models.URLField(max_length=200, blank=True)
    
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True,
    )

    def __str__(self):
        #return username
        return str(self.user)