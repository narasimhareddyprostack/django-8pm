from django import forms
from empapp.models import User


class EmpForm(forms.Form):
    eid = forms.IntegerField(label="Id")
    ename = forms.CharField(label="Name")
    eloc = forms.CharField(label="Location")
    esal = forms.CharField(label="Salary")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
