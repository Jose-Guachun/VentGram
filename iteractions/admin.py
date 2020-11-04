from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
#model
from users.models import Relationship

# Register your models here.
admin.site.register(Relationship)