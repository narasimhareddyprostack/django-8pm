from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def getindex(request):
    print(request)
    return HttpResponse("index page")


def getaboutpage(request):
    return HttpResponse("<h1>About Page</h1>")


def getservicepage(request):
    return HttpResponse("Service Page")


def getcontactpage(request):
    return HttpResponse('Contact Page')
