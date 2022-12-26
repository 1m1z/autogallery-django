# Generated by Django 4.1.4 on 2022-12-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_carsmodel_carsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleCarmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarsMileage', models.IntegerField()),
                ('CarsTransmision', models.IntegerField(choices=[(1, 'Automatic'), (2, 'Manual')], default=2)),
                ('Cars_Seats', models.IntegerField(choices=[(1, '2'), (2, '4'), (3, '5')], default=2)),
                ('CarsLuggage', models.IntegerField(choices=[(1, '2'), (2, '3'), (3, '4'), (4, '5')], default=2)),
                ('Cars_Fuel', models.IntegerField(choices=[(1, 'gas'), (2, 'Petrol'), (3, 'electric'), (4, 'hybrid(Patrol & gas)'), (5, 'hybrid(Patrol & electric)')], default=3)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.carsmodel')),
            ],
        ),
    ]