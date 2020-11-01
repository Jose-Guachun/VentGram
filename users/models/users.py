#dependencias de django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.core import validators

#Utilities
from utils.models import CRideModel

class UserManager(BaseUserManager):

    def _create_user(self, email, username, first_name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
    	    **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields	):
        return self._create_user(email, username, first_name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, username, first_name, last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """User model
    extends from Django AbstarctBaseUser, change the username field
    to email and some extra fields.
    """

    email=models.EmailField(
        'Correo Electronico', 
        unique=True, 
        error_messages={
            'unique': 'Correo electronico en uso.'
        }
    )
    username=models.CharField(
        'Nombre de Usuario', 
        unique=True, 
        max_length=20,
        validators=[validators.MinLengthValidator(3)],
        error_messages={
            'unique': 'Nombre de Usuario en uso'
        }
    )
    first_name = models.CharField('Nombres', max_length=30, validators=[validators.MinLengthValidator(3)])
    last_name = models.CharField('Apellidos', max_length=30,validators=[validators.MinLengthValidator(3)])
    code=models.CharField(
        'code', 
        max_length=100, 
        unique=True, blank=True, null=True,
        error_messages={
            'unique': 'Codigo en uso'
        }
        )

    is_admin=models.BooleanField(
        'Es Administrador',
        default=True,
        help_text=(
            'help easily distinguish users and perform queries. '
            'Clients are the main type of user. '
        )
    )

    is_verified=models.BooleanField(
        'Email Verificado',
        default=False,
        help_text=('se establece en verdadero cuando el usuario ha verificado su dirección de correo electrónico',
        )
    )
    date_joined = models.DateTimeField('Fecha de Registro', default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name', ]


    def __str__ (self):
        return self.username
        
    
