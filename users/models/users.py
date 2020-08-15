#dependencias de django
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

#Utilities
from utils.models import CRideModel

class User(CRideModel ,AbstractUser):
    """User model
    extends from Django Abstarct User, change the username field
    to email and some extra fields.
    """
    email=models.EmailField(
        'email address', 
        unique=True, 
        error_messages={
            'unique': 'Correo electronico en uso.'
        }
        )
    is_client=models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'help easily distinguish users and perform queries. '
            'Clients are the main type of user. '
        )
    )

    is_verified=models.BooleanField(
        'verified',
        default=True,
        help_text='se establece en verdadero cuando el usuario ha verificado su dirección de correo electrónico',
    )

    code=models.CharField(max_length=20)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__ (self):
        return self.username
        
    
