from django.shortcuts import render
from .models import CarsModel

def homepage(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"home/home.html",context)


def carshow(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"Products/cars.html",context)