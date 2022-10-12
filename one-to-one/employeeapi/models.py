from django.db import models

# Create your models here.

class vehicle(models.Model):
    emp = models.CharField(max_length=100,null=True)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    Vehicle = models.OneToOneField(vehicle,on_delete = models.CASCADE,default="")
    
    

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE


#Data integrity options:
#Since we are creating models which depend on other models, we need to define the behavior of a record in one model when the corresponding record in the other is deleted. This is achieved by adding an optional on_delete parameter in the relational field, which can take the following values:

#on_delete = models.CASCADE – This is the default value. It automatically deletes all the related records when a record is deleted.(e.g. when an Album record is deleted all the Song records related to it will be deleted)
#on_delete = models.PROTECT – It blocks the deletion of a record having relation with other records.(e.g. any attempt to delete an Album record will be blocked)
#on_delete = models.SET_NULL – It assigns NULL to the relational field when a record is deleted, provided null = True is set.
#on_delete = models.SET_DEFAULT – It assigns default values to the relational field when a record is deleted, a default value has to be provided.
#on_delete = models.SET() – It can either take a default value as parameter, or a callable, the return value of which will be assigned to the field.
#on_delete = models.DO_NOTHING – Takes no action. Its a bad practice to use this value.
