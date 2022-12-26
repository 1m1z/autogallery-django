from django.shortcuts import render
from Home.models import CarsModel,SingleCarmodel
def carslist(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"Products/cars.html",context)

def carsingle(request , car_id):
    scar = SingleCarmodel.objects.get(pk = car_id)
    
    context={
        "cars":scar
    }

    return render(request,"Products/singlecar.html",context)