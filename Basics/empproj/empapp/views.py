from django.shortcuts import render
from empapp.forms import EmployeeForm, UserForm
from empapp.models import Employee, User
# Create your views here.


def gethomepage(request):
    return render(request, 'home.html')


def getempregpage(request):
    empform = EmployeeForm()
    return render(request, 'emp.html', {'empform': empform})


def saveempview(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        esal = request.POST['esal']
        empdata = Employee(eid=eid, ename=ename, esal=esal)
        empdata.save()
        # print(eid, ename, esal)

    return render(request, 'success.html')


""" def saveempview(request):
    if request.method == 'POST':
        empdata = EmployeeForm(request.POST)
        if (empdata.is_valid()):
            empdata.save()

    return render(request, 'success.html') """


def getnewuserpage(request):
    userform = UserForm()
    return render(request, 'user.html', {'userform': userform})


def saveuserview(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        uloc = request.POST.get('uloc')
        userdata = User(uname=uname, uloc=uloc)
        userdata.save()

    return render(request, 'success.html')
