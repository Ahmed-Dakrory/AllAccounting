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



class acc_code_With_details(models.Model):
    account = models.ForeignKey(acc_code, on_delete=models.PROTECT)
    Type = models.BooleanField(default=False,null=True)
    price = models.CharField(max_length=500,default=None,null=True)
    note = models.CharField(max_length=500,default=None,null=True)
    currency = models.CharField(max_length=500,default=None,null=True)
    
    deleted =  models.BooleanField(default=False,null=True)

    
    class Meta:
       db_table = "acc_code_With_details"

    def to_json(self):
        return {
            'account':self.account.Name,
            'accountNumber':self.account.id,
            'id':self.id,
            'price':self.price,
            'note':self.note,
            'currency':self.currency,
            'Type':self.Type
        }
    

class transaction(models.Model):
    maqbodat = models.ForeignKey(acc_code, on_delete=models.PROTECT,related_name='maqbodat')
    madfo3at = models.ForeignKey(acc_code, on_delete=models.PROTECT,related_name='madfo3at')
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    Notes = models.TextField(default=None,null=True)
    Doc_Number = models.CharField(max_length=500,default=None,null=True)
    Qyed_Number = models.CharField(max_length=500,default=None,null=True)
    Check_Number = models.CharField(max_length=500,default=None,null=True)
    maqbodat_Total = models.CharField(max_length=500,default=None,null=True)
    madfo3at_Total = models.CharField(max_length=500,default=None,null=True)
    
    acc_codes_With_details_maqbodat = models.ManyToManyField(acc_code_With_details,related_name='maqbodat_acc_codes')
    acc_codes_With_details_madfo3at = models.ManyToManyField(acc_code_With_details,related_name='madfo3at_acc_codes')
    
    deleted =  models.BooleanField(default=False,null=True)


    class Meta:
       db_table = "transaction"


    def to_json(self):
        return {
            'id':self.id,
            'maqbodatId':self.maqbodat.id,
            'madfo3atId':self.madfo3at.id,
            'Notes':self.Notes,
            'acc_codes_With_details_maqbodat' : [item.to_json() for item in self.acc_codes_With_details_maqbodat.all()],
            'acc_codes_With_details_madfo3at' : [item.to_json() for item in self.acc_codes_With_details_madfo3at.all()],
            'date':self.date,
            'Doc_Number':self.Doc_Number,
            'Qyed_Number':self.Qyed_Number,
            'Check_Number':self.Check_Number,
            'maqbodat_Total':self.maqbodat_Total,
            'madfo3at_Total':self.madfo3at_Total
        }

