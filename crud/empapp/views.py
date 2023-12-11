from django.shortcuts import render, redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee
# Create your views here.


def createempview(request):
    if request.method == 'POST':
        empdata = EmployeeForm(request.POST)
        if empdata.is_valid():
            try:
                empdata.save()
                return redirect("/read")
            except:
                pass
    else:
        empform = EmployeeForm()
    return render(request, 'create.html', {'empform': empform})


def displayempview(request):
    employees = Employee.objects.all()
    return render(request, 'display.html', {'employees': employees})


def updateempview(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        empdata = EmployeeForm(request.POST, instance=employee)
        try:
            empdata.save()
            return redirect('/read')
        except:
            pass

    return render(request, 'update.html', {'employee': employee})


def deleteempview(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("/read")
