from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def contactus(request):
    menutemplate = loader.get_template('Contact/contactus.html')
    return HttpResponse(menutemplate.render())