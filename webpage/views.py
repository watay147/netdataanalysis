#encoding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from .models import company
from django.db.models import Q

# Create your views here.

def index(request):
    topcredit_list=company.objects.all()
    attention_list=topcredit_list
    context = {'topcredit_list': topcredit_list,'attention_list':attention_list}
    return render(request,'index.html', context)

def indexcreditorders(request):
    return render(request,'index.html')

def indexevents(request):
    return render(request,'index.html')

def indexnews(request):
    return render(request,'index.html')

def indexattentions(request):
    return render(request,'index.html')
def indexsearch(request):
    company_list=company.objects.filter(Q(name__icontains=request.GET['item'])|Q(stockno__icontains=request.GET['item']))
    #company_list+=company.objects.filter(stockno__startswith=request.GET['item'])
    context={'company_list':company_list}
    return render(request,'indexsearch.html',context)

def viewcompany(request,stockno):
    name=company.objects.all()[0].description
    return HttpResponse(stockno+':'+name)

def viewevents(request,id):
    return HttpResponse(eventsid)

def viewnews(request,id):
    return HttpResponse(eventsid)




