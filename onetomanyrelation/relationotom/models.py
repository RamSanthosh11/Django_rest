from ast import Delete
from pyexpat import model
from tkinter import Place
from django.db import models

# Create your models here.
class phone(models.Model):
    mobile=models.CharField(max_length=100)
    email = models.EmailField(max_length=250,default = "GFG is best")

class person(models.Model):
    Name=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Mobile=models.ForeignKey(phone,on_delete=models.CASCADE)


class aadar(models.Model):
    aName=models.CharField(max_length=100)
    anumber=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Mobile=models.ForeignKey(phone,on_delete=models.CASCADE)


    