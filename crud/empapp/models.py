from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=32)
    ename = models.CharField(max_length=32)
    esal = models.IntegerField()
    eemail = models.EmailField()

    class Meta:
        db_table = "employee"


# empapp_employee
# employee
