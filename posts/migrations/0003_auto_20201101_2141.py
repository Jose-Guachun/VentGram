# Generated by Django 3.0.5 on 2020-11-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201101_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
    ]
