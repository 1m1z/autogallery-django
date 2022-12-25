# Generated by Django 4.1.4 on 2022-12-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_singlecarmodel_carsluggage_singlecarmodel_cars_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlecarmodel',
            name='Cars_Fuel',
            field=models.IntegerField(choices=[(1, 'gas'), (2, 'Petrol'), (3, 'electric'), (4, 'hybrid(Patrol & gas)'), (5, 'hybrid(Patrol & electric)')], default=3),
        ),
    ]
