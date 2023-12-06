from django.shortcuts import render
from empapp.forms import EmpForm, UserForm
# Create your views here.


def gethomepage(request):
    mydata = {'msg': 'Good Mornig'}
    return render(request, 'home.html', context=mydata)


def getempregpage(request):
    empform = EmpForm()
    return render(request, 'emp.html', {'empform': empform})


def getuserregpage(request):
    userform = UserForm()
    return render(request, 'user.html', {'userform': userform})
