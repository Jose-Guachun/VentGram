# Generated by Django 3.0.5 on 2020-11-05 00:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import posts.models.category
import posts.models.project


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at')),
                ('category', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(5)])),
                ('image', models.ImageField(upload_to=posts.models.category.ruta_imagen_Category)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at')),
                ('status', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5)])),
                ('image', models.ImageField(upload_to=posts.models.category.ruta_imagen_Status)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en el que se modifico el objeto', verbose_name='modified at')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(125)])),
                ('objetive', models.TextField(validators=[django.core.validators.MinLengthValidator(15)])),
                ('image', models.ImageField(upload_to=posts.models.project.ruta_imagen)),
                ('label', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('website', models.URLField(blank=True)),
                ('document', models.FileField(upload_to=posts.models.project.ruta_documento)),
                ('collaborators', models.CharField(blank=True, max_length=300, validators=[django.core.validators.MinLengthValidator(5)])),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
