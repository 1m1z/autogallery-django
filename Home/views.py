from django.shortcuts import render
from Products.models import CarsModel
from Blog.models import PostModel


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


<<<<<<< HEAD
=======

def postlist(request):
    Post = PostModel.objects.all()

    context={
        "posts":Post
    }
    return render(request,"Blog/post.html",context)


def singlepost(request , post_id):
    spost = PostModel.objects.get(pk = post_id)

    context={
        "sposts":spost
    }

    return render(request,"Blog/singlepost.html",context)

def postlistHome(request):
    Post = PostModel.objects.all()

    context={
        "posts":Post
    }
    return render(request,"/Home/home.html",context)







# scar = CarsModel.objects.get(pk = car_id) 


# def singlecar(request,car_id):
#     scar = SingleCarmodel.objects.filter(pk = car_id)
    
#     context={
#         "scars":scar
#     }

#     return render(request,"Products/singlecar.html",context)
>>>>>>> 1406b8a8fa4849c72a7c87e7f2d6d4a4991bea71


