# Generated by Django 3.0.7 on 2020-11-13 15:37

import VentGram.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models.profile


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': 'Correo electronico en uso.'}, max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('username', models.CharField(error_messages={'unique': 'Nombre de Usuario en uso'}, max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre de Usuario')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Apellidos')),
                ('code', models.CharField(blank=True, error_messages={'unique': 'Codigo en uso'}, max_length=100, null=True, unique=True, verbose_name='code')),
                ('is_admin', models.BooleanField(default=True, help_text='help easily distinguish users and perform queries. Clients are the main type of user. ', verbose_name='Es Administrador')),
                ('is_verified', models.BooleanField(default=False, help_text=('se establece en verdadero cuando el usuario ha verificado su dirección de correo electrónico',), verbose_name='Email Verificado')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Registro')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_province', models.CharField(blank=True, max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at')),
                ('dni', models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10), VentGram.validators.vcedula])),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.MinLengthValidator(10), VentGram.validators.SoloNumeros])),
                ('education_level', models.CharField(blank=True, max_length=50)),
                ('work_area', models.CharField(blank=True, max_length=100)),
                ('home_address', models.CharField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=users.models.profile.ruta)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Country')),
                ('favorites', models.ManyToManyField(related_name='favorites', to='posts.Project')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Province')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Province'),
        ),
    ]
