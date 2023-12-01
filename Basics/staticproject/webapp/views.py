from django.shortcuts import render

# Create your views here.


def getindexpage(request):
    return render(request, 'index.html')


def getaboutpage(request):
    return render(request, 'about.html')


def getservicepage(request):
    return render(request, 'service.html')


def getcontactpage(request):
    return render(request, 'contact.html')
