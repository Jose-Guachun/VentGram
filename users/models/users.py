#dependencias de django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.db import models


#Utilities
from utils.models import CRideModel

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user=self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin=True
        user.save()
        return user    



class User(CRideModel ,AbstractBaseUser):
    """User model
    extends from Django AbstarctBaseUser, change the username field
    to email and some extra fields.
    """

    email=models.EmailField(
        'email address', 
        unique=True, 
        error_messages={
            'unique': 'Correo electronico en uso.'
        }
    )
    username=models.CharField(
        'username', 
        unique=True, 
        max_length=150,
        error_messages={
            'unique': 'Nombre de Usuario en uso'
        }
    )
    first_name = models.CharField('first name', max_length=150, blank=True, null=True)
    last_name = models.CharField('last name', max_length=150, blank=True, null=True)
    code=models.CharField(
        'code', 
        max_length=20, 
        unique=True, blank=True, null=True,
        error_messages={
            'unique': 'Codigo en uso'
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
        help_text=('se establece en verdadero cuando el usuario ha verificado su dirección de correo electrónico',
        )
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name', ]


    def __str__ (self):
        return self.username
        
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
