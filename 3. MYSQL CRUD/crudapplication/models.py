from django.db import models

# Create your models here.
class Employee(models.Model):
    eid= models.CharField(max_length=23)
    ename = models.CharField(max_length=123)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=12)
    class Meta:
        # this will be our database name that we want to put and in this class always put table name 
        db_table = "employee"