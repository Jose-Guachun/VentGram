# Generated by Django 3.0.5 on 2020-10-04 22:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ('image', models.ImageField(upload_to='category/photos/%Y/%m/%d/')),
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
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('objetive', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='project/photos/%Y/%m/%d/')),
                ('status', models.CharField(max_length=30)),
                ('website', models.URLField(blank=True)),
                ('document', models.FileField(upload_to='project/doc/%Y/%m/%d/')),
                ('collaborators', models.CharField(blank=True, max_length=300, validators=[django.core.validators.MinLengthValidator(5)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
