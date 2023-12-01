from django.db import models

# Create your models here.


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=24)
    esal = models.FloatField()


class User(models.Model):
    uno = models.IntegerField()
    name = models.CharField(max_length=32)
    loc = models.CharField(max_length=25)
