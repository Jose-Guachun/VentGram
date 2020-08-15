#django
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

#utilities
from utils.models import CRideModel

class Profile(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE,)
    city=models.ForeignKey('users.City', on_delete=models.CASCADE, blank=True, null=True)
    
    dni=models.CharField(max_length=10, blank=True)
    gender=models.CharField(max_length=20, blank=True)
    birth_date=models.DateField(blank=True, null=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20, blank=True)
    education_level=models.CharField(max_length=50, blank=True)
    work_area=models.CharField(max_length=100, blank=True)
    profile=models.CharField(max_length=50, blank=True)
    
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True,
    )

    def __str__(self):
        #return username
        return str(self.user)