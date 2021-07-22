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
    if request.method=='POST':
        madfo3at_idSelectedData = request.POST['madfo3at_idSelected']
        maqbodat_idSelectedData = request.POST['maqbodat_idSelected']

        
        maqbodatData = acc_code.objects.get(pk=maqbodat_idSelectedData)
        madfo3atData = acc_code.objects.get(pk=madfo3at_idSelectedData)

        dateData = request.POST['date']
        QyedData = request.POST['Qyed']
        docNumberData = request.POST['docNumber']
        checkNumberData = request.POST['checkNumber']
        notesData = request.POST['notes']
        totalEnterData = request.POST['totalEnter']
        totaloutData = request.POST['totalout']


        madfo3at_allLengthData = request.POST['madfo3at_allLength']
        maqbodat_allLengthData = request.POST['maqbodat_allLength']

        reqtransaction = transaction.objects.create(maqbodat=maqbodatData,madfo3at=madfo3atData,
                        Doc_Number= docNumberData,Qyed_Number=QyedData,Check_Number=checkNumberData,
                        Notes=notesData,maqbodat_Total=totaloutData,madfo3at_Total=totalEnterData)
        reqtransaction.save()

        for madfo3at_i in range(0,int(madfo3at_allLengthData)):
            madfo3at_elementId = request.POST['madfo3ataccountDivLen_'+str(madfo3at_i)]
            
            madfo3at_elementData = acc_code.objects.get(pk=madfo3at_elementId)
            madfo3at_accountNote = request.POST['accountNote_'+str(madfo3at_elementId)]
            madfo3at_accountPrice = request.POST['accountPrice_'+str(madfo3at_elementId)]
            madfo3at_accountCurrency = request.POST['accountCurrency_'+str(madfo3at_elementId)]

            if madfo3at_accountPrice!='0':
                acc_code_With_detailsToAdd = acc_code_With_details.objects.create(account=madfo3at_elementData, Type=True
                            ,price=madfo3at_accountPrice,note=madfo3at_accountNote,currency=madfo3at_accountCurrency)
                acc_code_With_detailsToAdd.save()
                reqtransaction.acc_codes_With_details_madfo3at.add(acc_code_With_detailsToAdd)

        for maqbodat_i in range(0,int(maqbodat_allLengthData)):
            maqbodat_elementId = request.POST['maqbodataccountDivLen_'+str(maqbodat_i)]
            
            maqbodat_elementData = acc_code.objects.get(pk=maqbodat_elementId)
            maqbodat_accountNote = request.POST['accountNote_'+str(maqbodat_elementId)]
            maqbodat_accountPrice = request.POST['accountPrice_'+str(maqbodat_elementId)]
            maqbodat_accountCurrency = request.POST['accountCurrency_'+str(maqbodat_elementId)]

            if maqbodat_accountPrice!='0':
                acc_code_With_detailsToAdd = acc_code_With_details.objects.create(account=maqbodat_elementData, Type=True
                            ,price=maqbodat_accountPrice,note=maqbodat_accountNote,currency=maqbodat_accountCurrency)
                acc_code_With_detailsToAdd.save()
                reqtransaction.acc_codes_With_details_maqbodat.add(acc_code_With_detailsToAdd)

    
    allTransactions = transaction.objects.all()
    context = {
        'allTransactions':allTransactions
    }
    return render(request,'qyod/qyod.html',context)


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
            if typeData=='false':
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
            if typeData=='false':
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
    treeType=request.GET['treeType']
    print(treeType)
    if id=='#':
        allJson = []
        allData = None
        if treeType=='0':
            allData = acc_code.objects.filter(Q(Level=1) & (Q(Ekfal=0) |Q(Ekfal=2) |Q(Ekfal=3) ) & Q(deleted=False))
        elif treeType == '1':
            allData = acc_code.objects.filter(Q(Level=1) & (Q(Ekfal=1) |Q(Ekfal=2) |Q(Ekfal=3) ) & Q(deleted=False))
            
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


def getTransactionDetails(request):
    id=request.POST['id']
    allData = transaction.objects.get(id=id)
    allJson = {}
    allJson['Result'] = "Fail"
    if allData !=None:
        allJson['Data'] = allData.to_json()
           

    # print(allJson)
    if allJson != None:
        allJson['Result'] = "Ok"
        return JsonResponse(allJson, safe=False)
    else:
        allJson['Result'] = "Fail"
        return JsonResponse(allJson, safe=False)


def getAllElementsRelatedToTreeElementAndType(request):
    id=request.POST['id']
    typeOfTree=request.POST['Type']
    if typeOfTree=='0':
        typeOfTree=False
    elif typeOfTree == '1':
        typeOfTree=True
    
    Data = acc_code.objects.filter(Q(relatedToId=id) & Q(Type = typeOfTree))

    allData = {}
    if Data !=None:
        array = []
        for item in list(Data):
            DataReg=item.element_to_json()
            array.append(DataReg)
        allData['length'] = len(array)
        allData['output'] = array
    else:
        
        allData['length'] = 0
        allData['output'] = None
    
    allData['Result'] = "Ok"
    if allData != None:
        return JsonResponse(allData, safe=False)
    else:
        allData['Result'] = "Fail"
        return JsonResponse(allData, safe=False)




