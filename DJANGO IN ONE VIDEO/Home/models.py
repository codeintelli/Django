from django.db import models
from datetime import datetime
# Create your models here.

# makemigration:- make migration and store in a file
# migrate:- apply the pending changes created by makemigration and generate a file 

""" 
1. you have to create a model in which you have to declare field of that model
eg. class TableName(models.Model):
    field = models.datatype(length,default,helptext,null=true/false,blank=true/false)
after creating it register it into Home.admin
    from Home.models import Contact
    # Register your models here.
    admin.site.register(Contact)
after that go to apps.py and take HomeConfig and paste into project folder and go to setting and then paste it into "installed Apps"

'Home.apps.HomeConfig',

migrate it using makemigration and then migrate it 

 """
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(blank=True, default=datetime(1111, 11, 11), null=True, help_text="Today Date.")

    def __str__(self):
        return self.name + "\t<"+ self.email +">"