from django.shortcuts import render

# Create your views here.



def loadMainPageForaccounting(request):
    return render(request,'accountingindex.html',None)



def qyod(request):
    return render(request,'qyod/qyod.html',None)


def qyodUSA(request):
    return render(request,'qyod/qyodUSA.html',None)


def qyodReport(request):
    return render(request,'qyod/qyodReport.html',None)