from django import forms
from empapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        # fields = ['eid', 'ename', 'esal']


class UserForm(forms.Form):
    uname = forms.CharField(max_length=32, label="User Name")
    uloc = forms.CharField(max_length=32, label="Location")
