from django.db import models

# Create your models here.


class User(models.Model):
    uname = models.CharField(max_length=32)
    uemail = models.CharField(max_length=32)
    uloc = models.CharField(max_length=32)
