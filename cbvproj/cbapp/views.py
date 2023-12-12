from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class HelloWorldView(View):
	def get(self,request):
	    return HttpResponse("<h1>HelloWorld-class</h1>")


def getHelloworld(request):
    return HttpResponse("<h1>HelloWorld-fun</h1>")