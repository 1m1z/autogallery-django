# Generated by Django 4.1.4 on 2022-12-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_singlecarmodel_carsserial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlecarmodel',
            name='car',
        ),
        migrations.AddField(
            model_name='singlecarmodel',
            name='car',
            field=models.ManyToManyField(null=True, to='Home.carsmodel'),
        ),
    ]
