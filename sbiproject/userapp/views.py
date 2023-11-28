from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexpage(request):
    return HttpResponse("Index Page")


def servicepage(request):
    return HttpResponse("Service Page")


def productpage(request):
    return HttpResponse("Product Page")


def contactpage(request):
    return HttpResponse("Contact Page")
