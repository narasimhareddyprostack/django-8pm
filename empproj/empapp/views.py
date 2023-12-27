from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from empapp.models import Employee
from empapp.serializers import EmployeeSerializer
# Create your views here.

'''
API URL : API URL : 127.0.0.1:8000/api/create
'''


@api_view(['POST'])
def createemp(request):
    empSerializer = EmployeeSerializer(data=request.data)
    if empSerializer.is_valid():
        empSerializer.save()
    return Response(empSerializer.data)


'''
API URL : API URL : 127.0.0.1:8000/api/
'''


@api_view(['GET'])
def getemployees(request):
    empdata = Employee.objects.all()
    print(type(empdata))
    empSerializer = EmployeeSerializer(empdata, many=True)
    return Response(empSerializer.data)
    # return Response({'status': 200, 'message': 'Getting all Employees'})


'''
API URL : API URL : 127.0.0.1:8000/api/update/<int:id>
'''


@api_view(['POST'])
def updateemp(request, id):
    empdata = Employee.objects.get(id=id)
    empSerializer = EmployeeSerializer(instance=empdata, data=request.data)
    if empSerializer.is_valid():
        empSerializer.save()

    return Response(empSerializer.data)


'''
API URL : API URL : 127.0.0.1:8000/api/delete/1
'''


@api_view(['DELETE'])
def deleteemp(request, id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()

    return Response({'message': 'Employee Deleted Successfully'})


def dispalyEmployee(request):
    emp_list = Employee.objects.all()
    emp_dict = {'emp_list': emp_list}
    return render(request, 'emp.html', context=emp_dict)
