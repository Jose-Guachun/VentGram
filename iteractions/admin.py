from django.contrib import admin
from django.db import models

#model
from iteractions.models import Relationship, Likes

# Register your models here.
admin.site.register(Relationship)
admin.site.register(Likes)