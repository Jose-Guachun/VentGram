# Generated by Django 3.0.5 on 2020-09-28 22:34

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modified',
        ),
        migrations.AddField(
            model_name='profile',
            name='home_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dni',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10), users.validators.SoloNumeros]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.MinLengthValidator(10), users.validators.SoloNumeros]),
        ),
        migrations.AlterField(
            model_name='social_net',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='social_net',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True, help_text='help easily distinguish users and perform queries. Clients are the main type of user. ', verbose_name='client status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, help_text=('se establece en verdadero cuando el usuario ha verificado su dirección de correo electrónico',), verbose_name='verified'),
        ),
    ]
