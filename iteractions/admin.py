from django.contrib import admin
from django.db import models

#model
from iteractions.models import Relationship, Likes, Comment, Message

admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'user',
        'recipient')
        
# Register your models here.
admin.site.register(Relationship)
admin.site.register(Likes)
admin.site.register(Comment)

