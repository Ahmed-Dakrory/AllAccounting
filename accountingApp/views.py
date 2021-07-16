from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import SuspiciousOperation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


import json
import threading
from django.db.models import Count
from django.db.models import Q
from accountingApp.models import *
# Create your views here.



def loadMainPageForaccounting(request):
    return render(request,'accountingindex.html',None)



def qyod(request):
    return render(request,'qyod/qyod.html',None)


def qyodUSA(request):
    return render(request,'qyod/qyodUSA.html',None)


def qyodReport(request):
    return render(request,'qyod/qyodReport.html',None)




@login_required
def dalel(request):
    if request.method=='POST':
        typeOfReq = request.POST['typeOfEdit']

        


        if typeOfReq == 'edit':
            accountName = request.POST['accountName']
            accountNumber = request.POST['accountNumber']
            typeData = request.POST['type']
            NormalData = request.POST['Normal']
            ekfalData = request.POST['ekfal']

            if accountNumber == '':
                accountNumber = None
            typeData = request.POST['type']
            if typeData=='0':
                typeData=False
            else:
                typeData=True
            dataToInsert = acc_code.objects.filter(Q(id=accountNumber)  & Q(deleted=False))
            dataToInsert.update(Name=accountName,Type=typeData,Normal=NormalData,Ekfal=ekfalData)
        elif typeOfReq =='new':
            # accountName = request.POST['accountName']
            accountNumber = request.POST['accountNumber']
            LevelData = request.POST['LevelData']
            LevelData = 1+int(LevelData)
            if accountNumber == '':
                accountNumber = None
            typeData = request.POST['type']
            if typeData=='0':
                typeData=False
            else:
                typeData=True
            NormalData = request.POST['Normal']
            ekfalData = request.POST['ekfal']
            print('donedone')
            dataToInsert = acc_code.objects.create(Name="جديد",relatedToId=accountNumber,
            Type=typeData,Normal=NormalData,Ekfal=ekfalData,Level=LevelData)
            dataToInsert.save()

    

        
    dataToReturn = {
        "typeOfEdit":"Nothing",
        "LevelData":0
    }

    return render(request,'dalel/dalel.html',dataToReturn)


def arseda(request):
    return render(request,'dalel/arseda.html',None)



def treeOfMain(request):
    id=request.GET['id']
    normal=request.GET['Normal']
    if id=='#':
        allJson = []
        allData = acc_code.objects.filter(Q(Level=1) & Q(Normal=normal) & Q(deleted=False))

        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())
           
    else:
        relatedToId = id.replace('element','')
        print(relatedToId)
        allJson = []
        allData = acc_code.objects.filter(Q(relatedToId=relatedToId) & Q(deleted=False))
        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())

    # print(allJson)
    if allJson != None:
        return JsonResponse(allJson, safe=False)
    else:
        allJson['Result'] = "Fail"
        return JsonResponse(allJson, safe=False)


def treeOfMainAll(request):
    id=request.GET['id']
    if id=='#':
        allJson = []
        allData = acc_code.objects.filter(Q(Level=1) & Q(deleted=False))

        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())
           
    else:
        relatedToId = id.replace('element','')
        print(relatedToId)
        allJson = []
        allData = acc_code.objects.filter(Q(relatedToId=relatedToId) & Q(deleted=False))
        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())

    # print(allJson)
    if allJson != None:
        return JsonResponse(allJson, safe=False)
    else:
        allJson['Result'] = "Fail"
        return JsonResponse(allJson, safe=False)




def delete_treeElement(request):
    objectId = request.POST['id']


    objectDetails=acc_code.objects.filter(Q(id=objectId) & Q(deleted=False))
    objectDetails.update(deleted = True)

   
    allJson = {"Result": "Fail"}
    
    allJson['Result'] = "Success"


    if allJson != None:
        return JsonResponse(allJson, safe=False)
    else:
        allJson['Result'] = "Fail"
        return JsonResponse(allJson, safe=False)

def getElementParametersOfTree(request):
    id=request.POST['id']
    Data = acc_code.objects.get(id=id)
    allData = {}
    if Data !=None:
        DataReg=Data.element_to_json()
        if Data.relatedToId !=None:
            MainAccount = acc_code.objects.get(id=Data.relatedToId).element_to_json()
            DataReg['relatedToId'] = MainAccount
        else:
            DataReg['relatedToId'] = None
        allData['output'] = DataReg
    else:
        allData['output'] = None
    
    allData['Result'] = "Ok"
    if allData != None:
        return JsonResponse(allData, safe=False)
    else:
        allData['Result'] = "Fail"
        return JsonResponse(allData, safe=False)