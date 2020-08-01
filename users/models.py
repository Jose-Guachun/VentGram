#dependencias de django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Red_Social(models.Model):
    red_social=models.URLField(max_length=200, blank=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

class Pais(models.Model):
    pais=models.CharField(max_length=50, blank=True)

    def __str__(self):
    #return username
        return self.pais

class Provincia(models.Model):
    pais=models.ForeignKey(Pais, on_delete=models.CASCADE)
    provincia=models.CharField(max_length=50, blank=True)

    def __str__(self):
    #return username
        return self.provincia
    
class Ciudad(models.Model):
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50, blank=True)

    def __str__(self):
    #return username
        return self.ciudad
    
class Profile(models.Model):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=True, null=True)

    genero=models.CharField(max_length=20, blank=True)
    fecha_nacimiento=models.DateField(blank=True, null=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20, blank=True)
    nivel_educativo=models.CharField(max_length=50, blank=True)
    trabajo=models.CharField(max_length=100, blank=True)


    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True,
    )

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

def __str__(self):
    #return username
    return self.User.username


