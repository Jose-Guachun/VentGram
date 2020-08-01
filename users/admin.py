#clases de admin

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.db import models

#Models
from django.contrib.auth.models import User
from users.models import Profile, Ciudad, Pais, Provincia

# Register your models here.
admin.site.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'pais',)
    list_display_links=('pk', 'pais',)
    fieldsets=(
        ('Pais', {
            'fields':('pais'),
        })
        )

admin.site.register(Provincia)
class ProvinciadAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'pais',
        'provincia',)

admin.site.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'provincia',
        'ciudad',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'user',
        'ciudad',
        'genero',
        'fecha_nacimiento',
        'biography',
        'phone_number',
        'nivel_educativo',
        'trabajo',
        'picture',)

    list_display_links=('pk', 'user', 'ciudad',)

    list_editable=(
        'genero',
        'fecha_nacimiento',
        'biography',
        'phone_number',
        'nivel_educativo',
        'trabajo',
        'picture',)

    search_fields=(
        'user__email', 
        'user__username',
        'user__first_name', 
        'user__last_name',
        'phone_number',
        )

    list_filter=(
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets=(
        ('Profile', {
            'fields':
                (
                    'user', 'picture',
                    'genero',
                    'fecha_nacimiento','nivel_educativo',
                    'trabajo',
                    ),
        }),
        ('Extra info',{
            'fields':(
                ('phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields':(('created', 'modified'),),
        })
    )
    readonly_fields=('created', 'modified',)

class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin,)
