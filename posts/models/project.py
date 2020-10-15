#django
from django.db import models

#utilities
from utils.models import CRideModel
from users.models import User
from posts.models import Category

#validators
from django.core import validators
from VentGram.validators import SoloNumeros


class Project(CRideModel):
    #profile model
    #extencio de proxy model mas informacion en la base de datos
    user=models.ForeignKey(User, on_delete=models.CASCADE,)
    profile= models.ForeignKey('users.profile', on_delete=models.CASCADE,)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    title=models.CharField(max_length=50,)
    description=models.TextField(validators=[validators.MinLengthValidator(125)])
    objetive=models.TextField(validators=[validators.MinLengthValidator(15)])
    image=models.ImageField(upload_to='project/photos/%Y/%m/%d/',)
    status=models.CharField(max_length=30,)
    website=models.URLField(max_length=200, blank=True)
    document=models.FileField(upload_to='project/doc/%Y/%m/%d/',)
    collaborators=models.CharField(max_length=300, validators=[validators.MinLengthValidator(5)], blank=True)

    def __str__(self):
        return '{} por @{}'.format(self.title, self.user.username)