from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import SuspiciousOperation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
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

def treeOfMain(request):
    id=request.GET['id']
    normal=request.GET['Normal']
    if id=='#':
        allJson = []
        allData = acc_code.objects.filter(Q(Level=1) & Q(Normal=normal))

        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())
           
    else:
        relatedToId = id.replace('element','')
        print(relatedToId)
        allJson = []
        allData = acc_code.objects.filter(Q(relatedToId=relatedToId))
        listResult=list(allData)
        for result in listResult:
            allJson.append(result.element_to_json())

    # print(allJson)
    if allJson != None:
        return JsonResponse(allJson, safe=False)
    else:
        allJson['Result'] = "Fail"
        return JsonResponse(allJson, safe=False)
