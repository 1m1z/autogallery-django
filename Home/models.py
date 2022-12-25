from django.db import models

# Create your models here.
class CarsModel (models.Model):

    CarsImage=models.ImageField(upload_to= "cars/",null=True)
    CarsName=models.CharField(max_length=100)
    CarsModel=models.CharField(max_length=250)
    CarsSalary=models.IntegerField()

    # class Meta:
    #     abstract = True


    def __str__(self):
        return self.CarsName

class SingleCarmodel(models.Model):
    car = models.ForeignKey(CarsModel , on_delete=models.CASCADE)
    CarsMileage = models.IntegerField()

    Transmision_choices = (
        (1,'Automatic'),
        (2,'Manual'),
    )
    CarsTransmision = models.IntegerField(choices=Transmision_choices,default=2)

    Seats_choices= (
        (1,'2'),
        (2,'4'),
        (3,'5'),
    )

    Cars_Seats= models.IntegerField(choices=Seats_choices,default=2)
    Luggage_choices = (
        (1,'2'),
        (2,'3'),
        (3,'4'),
        (4,'5'),
    )
    CarsLuggage = models.IntegerField(choices=Luggage_choices,default=2)
    
    Fuel = (
        (1,'gas'),
        (2,'Petrol'),
        (3,'electric'),
        (4,'hybrid(Patrol & gas)'),
        (5,'hybrid(Patrol & electric)'),

    )
    Cars_Fuel = models.IntegerField(choices=Fuel,default=3)

    
    def __str__(self):
        return self.CarsName