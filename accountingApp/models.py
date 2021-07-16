from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
from uuid import uuid4
import os


# Create your models here.
class acc_code(models.Model):
    Name = models.CharField(max_length=500,default=None)
    Notes = models.TextField(default=None,null=True)
    Flag = models.CharField(max_length=500,default=None,null=True)
    Type = models.BooleanField(default=False,null=True)
    Ekfal =  models.CharField(max_length=500,default=None,null=True)
    Normal =  models.CharField(max_length=500,default=None,null=True)
    Level =  models.CharField(max_length=500,default=None,null=True)
    relatedToId =  models.IntegerField(default=None,null=True)
    Mem_Volume_M =  models.CharField(max_length=500,default=None,null=True)
    Mem_Volume_W =  models.CharField(max_length=500,default=None,null=True)
    Mem_Volume =  models.CharField(max_length=500,default=None,null=True)
    Mem_City =  models.CharField(max_length=500,default=None,null=True)
    Mem_Count =  models.CharField(max_length=500,default=None,null=True)
    Mem_Tel =  models.CharField(max_length=500,default=None,null=True)
    Mem_Tel =  models.CharField(max_length=500,default=None,null=True)
    Mem_Address =  models.TextField(default=None,null=True)
    Mem_Pay =  models.BooleanField(default=False,null=True)
    Mem_LDate =  models.CharField(max_length=500,default=None,null=True)
    deleted =  models.BooleanField(default=False,null=True)


    class Meta:
        db_table = "acc_code"


    def element_to_json(self):
        return {
            'accountNumber':self.id,
            'id' :"element"+str(self.id),
            'text' :self.Name,
            'Level':self.Level,
            'typeOfIcon':"file",
            'type':self.Type,
            "children" : True,
            "Ekfal":self.Ekfal,
            "Normal":self.Normal,
            "relatedToId":self.relatedToId
            }

    def __str__(self):
        return self.Name