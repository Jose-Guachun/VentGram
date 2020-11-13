from django.contrib import admin
from django.db import models

#model
from iteractions.models import Relationship, Likes, Comment

# Register your models here.
admin.site.register(Relationship)
admin.site.register(Likes)
admin.site.register(Comment)