from django.shortcuts import render
from Products.models import CarsModel
from Blog.models import PostModel



def homepage(request):
    car = CarsModel.objects.all()
    post = PostModel.objects.all()
    
    context={
        "cars":car,
        "posts" : post
    }

    return render(request,"home/home.html",context)




def carshow(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"Products/cars.html",context)


def singlecar(request,car_id):
    scar = CarsModel.objects.get(pk = car_id)
    
    context={
        "scars":scar
    }

    return render(request,"Products/singlecar.html",context)



def postlist(request):
    post = PostModel.objects.all()

    context={
        "posts":post
    }
    return render(request,"Blog/post.html",context)


def singlepost(request , post_id):
    spost = PostModel.objects.get(pk = post_id)

    context={
        "sposts":spost
    }

    return render(request,"Blog/singlepost.html",context)




