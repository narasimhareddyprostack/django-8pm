from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
# what is view, handle request and prepare resposne
# how to prepare response
# 1. using render
# 2. HttpResonse


def getindexpage(request):
    eid = 101
    ename = 'Rahul Gandhi'

    return render(request, 'index.html', context={'eid': eid, 'ename': ename})
    # return HttpResponse("Welcome to Djanog")


def getcontactpage(request):
    mydata = {'currenttime': datetime.datetime.now()}
    return render(request, 'contact.html', context=mydata)
