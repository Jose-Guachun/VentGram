# Generated by Django 3.0.5 on 2020-11-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20201101_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='views',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
