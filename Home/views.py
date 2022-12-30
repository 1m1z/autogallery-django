from django.shortcuts import render
from Products.models import CarsModel


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

def carshowdetails(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"Products/singlecar.html",context)

def singlecar(request,car_id):
    scar = CarsModel.objects.get(pk = car_id)
    
    context={
        "scars":scar
    }

    return render(request,"Products/singlecar.html",context)




