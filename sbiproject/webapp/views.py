from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def getpageone(request):
    return HttpResponse("Page One")


def getpagetwo(request):
    return HttpResponse("Page Two")
