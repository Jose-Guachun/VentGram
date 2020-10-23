#django
from django.db import models

#utilities
from utils.models import CRideModel
from users.models import User
from posts.models import Category

#validators
from django.core import validators
from VentGram.validators import SoloNumeros

def ruta_imagen(instance, file_name):
    route='{}/{}/{}/{}/{}'.format( 'users', instance.user.email, 'projects','img', file_name)
    return route

def ruta_documento(instance, file_name):
    route='{}/{}/{}/{}/{}'.format( 'users', instance.user.email, 'projects', 'document', file_name)
    return route

class Project(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.ForeignKey(User, on_delete=models.CASCADE,)
    profile= models.ForeignKey('users.profile', on_delete=models.CASCADE,)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    title=models.CharField(max_length=50,)
    description=models.TextField(validators=[validators.MinLengthValidator(125)])
    objetive=models.TextField(validators=[validators.MinLengthValidator(15)])
    image=models.ImageField(upload_to=ruta_imagen)
    status=models.CharField(max_length=30,)
    website=models.URLField(max_length=200, blank=True)
    document=models.FileField(upload_to=ruta_documento)
    collaborators=models.CharField(max_length=300, validators=[validators.MinLengthValidator(5)], blank=True)

    def __str__(self):
        return '{} por @{}'.format(self.title, self.user.username)