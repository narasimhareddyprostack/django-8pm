from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from drfapp.models import Employee
from drfapp.serializers import EmployeeSerializer
# Create your views here.

'''
    API URL: http://127.0.0.1:8000/
    Method:GET
    Required Fields: None
    ACCESS Type:Public
'''


@api_view(['GET'])
def home(request):
    emp_data = Employee.objects.all()
    emp_serializer = EmployeeSerializer(emp_data, many=True)
    # print(emp_data)
    # print(type(emp_data))
    print(type(emp_serializer.data))
    print(emp_serializer.data)
    return Response({'status': 200, 'message': 'Home page Response', 'avail': True, 'payload': emp_serializer.data})


'''
    API URL: http://127.0.0.1:8000/employees
    Method:GET
    Required Fields: None
    ACCESS Type:Public
'''


@api_view(['GET'])
def emp_data(request):
    emp_data = Employee.objects.all()
    emp_serializer = EmployeeSerializer(emp_data, many=True)

    return Response({'employees': emp_serializer.data})
