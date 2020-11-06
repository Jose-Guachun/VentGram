#django
from django.db import models
from django.utils.text import slugify


#utilities
from utils.models import CRideModel
from users.models import User
from posts.models import Category, Status

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
    status=models.ForeignKey(Status, on_delete=models.CASCADE)

    title=models.CharField('titulo',max_length=100)
    description=models.TextField(validators=[validators.MinLengthValidator(125)])
    objetive=models.TextField(validators=[validators.MinLengthValidator(15)])
    image=models.ImageField(upload_to=ruta_imagen)
    label=models.CharField(max_length=100, validators=[validators.MinLengthValidator(3)])
    website=models.URLField(max_length=200, blank=True)
    document=models.FileField(upload_to=ruta_documento)
    collaborators=models.CharField(max_length=300, validators=[validators.MinLengthValidator(5)], blank=True)
    url = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.url:
            project=Project.objects.first()
            if project is int:
                pk=project.pk
                pk+=1
            else:
                pk=1
            cadena = slugify(self.user)+slugify(pk)+'-'+slugify(self.title)
            while Project.objects.filter(url=cadena).exists():
                pk+=1
                cadena = slugify(self.user)+slugify(pk)+'-'+slugify(self.title)
            self.url=cadena
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return '{} por @{}'.format(self.title, self.user.username)


