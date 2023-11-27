from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def wish(request):
    return HttpResponse("Welcome to Django")


def index(request):
    return HttpResponse("Index Page")


def about(request):
    return HttpResponse("About Page")


def service(request):
    return HttpResponse("Service Page")
