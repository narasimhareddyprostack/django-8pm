from django.shortcuts import render
from empapp.models import Employee
# Create your views here.


def empdata(request):
    emp_list = Employee.objects.all()
    emp_dict = {'emp_list': emp_list}
    return render(request, 'emp.html', context=emp_dict)
